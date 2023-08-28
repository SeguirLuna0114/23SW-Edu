const express = require("express")
const app = express()
const mongoose = require("mongoose")
const mysql = require("sync-mysql");
const bodyParser = require("body-parser");
const env = require("dotenv").config({ path: "../../.env" });
const query = require("async");
const axios = require('axios');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// axios
//     .get('http://192.168.1.158:8000/select_clothes')
//     .then(res => {
//         console.log(`statusCode : ${res.status}`)
//         console.log(res)
//     })
//     .catch(error => {
//         console.log(error)
//     })

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});

// define schema
var new_clothes_Schema = mongoose.Schema({
    cloth_name: String,
    category: String,
    temp_min: String,
    temp_max: String
}, {
    versionKey: false
})

var new_places_Schema = mongoose.Schema({
    place_name: String,
    type: String,
    location: String
}, {
    versionKey: false
})

var rec_places_Schema = mongoose.Schema({
    location: String,
    date: String,
    place_name: String
}, {
    versionKey: false
})

// create model with mongodb collection and schema
var New_clohtes = mongoose.model('musinsas', new_clothes_Schema);
var New_places = mongoose.model('agodas', new_places_Schema);
var Rec_places = mongoose.model('rec_places', rec_places_Schema);

// mysql에서 뽑아온 추천 관광지를 mongodb에 바로 저장
app.post('/rec_place_insert', function (req, res, next) {
    const { loc, user_date } = req.body;
    const result = connection.query(
        "SELECT w.location, w.date, p.name AS place_name FROM weather w JOIN places p ON w.location = p.location AND w.temp_min <= p.temp_min WHERE w.location=? AND w.date=?;", [loc, user_date]);
    var location = [];
    var date = [];
    var place_name = [];

    for (let i = 0; i < result.length; i++) {
        location[i] = result[i]['location'];
        date[i] = result[i]['date'];
        place_name[i] = result[i]['place_name'];

        var rec_places = new Rec_places({ 'location': location[i], 'date': date[i], 'place_name': place_name[i] })

        rec_places.save(function (err, silence) {
            if (err) {
                res.status(500).send('insert error')
                console.log('{ "ok": false }');
                return;
            }
        })
    }
    res.writeHead(200);
    var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;" width="300px">
                <thead>
                    <tr><th>Location</th><th>Date</th><th>Place Name</th></tr>
                </thead>
                <tbody>
                `;
    for (var i = 0; i < result.length; i++) {
        template += `
        <tr>
            <td>${result[i]['location']}</td>
            <td>${result[i]['date']}</td>
            <td>${result[i]['place_name']}</td>
        </tr>
        `;
    }
    template += `
                </tbody>
            </table>
        </body>
        </html>
    `;
    res.end(template);
    console.log('{"ok":true,' + JSON.stringify(result) + ' }');
});


// list
app.get('/list', function (req, res, next) {
    New_clohtes.find({}, function (err, docs) {
        if (err) console.log('err')
        res.send(docs)
    })
});

app.get('/list2', function (req, res, next) {
    New_places.find({}, function (err, docs) {
        if (err) console.log('err')
        res.send(docs)
    })
});

// get
app.get('/get', function (req, res, next) {

    var userid = req.query.input
    User.findOne({ 'userid': userid }, function (err, doc) {
        if (err) console.log('err')
        res.send(doc)
    })
});

// new clothes insert from users
app.post('/cloth_insert', function (req, res, next) {
    var name = req.body.name;
    var category = req.body.category;
    var temp_min = req.body.temp_min;
    var temp_max = req.body.temp_max;
    var new_clothes = new New_clohtes({ 'cloth_name': name, 'category': category, 'temp_min': temp_min, 'temp_max': temp_max })

    new_clothes.save(function (err, silence) {
        if (err) {
            console.log('err')
            res.status(500).send('insert error')
            return;
        }
        //res.status(200)
        res.redirect('/select_clothes')
        console.log('{"ok":true,' + JSON.stringify(new_clothes) + ' }');
    })
});

// new places insert from users
app.post('/place_insert', function (req, res, next) {
    var place_name = req.body.place_name;
    var type = req.body.type;
    var location = req.body.location;
    var new_places = new New_places({ 'place_name': place_name, 'type': type, 'location': location })

    new_places.save(function (err, silence) {
        if (err) {
            console.log('err')
            res.status(500).send('insert error')
            return;
        }
        res.status(200)
        res.redirect('/select')
        console.log('{"ok":true,' + JSON.stringify(new_places) + ' }');
    })
    //res.redirect('/list')
});


// new clothes update from users
app.post('/cloth_update', function (req, res, next) {
    var cloth_name = req.body.cloth_name;
    var category = req.body.category;

    New_clohtes.findOne({ 'cloth_name': cloth_name }, function (err, new_clohtes) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        new_clohtes.cloth_name = cloth_name;
        new_clohtes.category = category;

        new_clohtes.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('update error')
                return;
            }
            res.status(200)
            res.redirect('/list')
            console.log('{"ok":true,' + JSON.stringify(new_clohtes) + ' }');
        })
    })
});

// new places update
app.post('/place_update', function (req, res, next) {
    var place_name = req.body.place_name;
    var type = req.body.type;
    var location = req.body.location;

    New_places.findOne({ 'place_name': place_name }, function (err, new_places) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        new_places.place_name = place_name;
        new_places.type = type;
        new_places.location = location;

        new_places.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('update error')
                return;
            }
            res.status(200)
            res.redirect('/list2')
            console.log('{"ok":true,' + JSON.stringify(new_places) + ' }');
        })
    })
});


// clothes delete
app.post('/cloth_delete', function (req, res, next) {
    var cloth_name = req.body.cloth_name;
    var new_clohtes = New_clohtes.find({ 'cloth_name': cloth_name })
    new_clohtes.remove(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send('delete error')
            return;
        }
        res.status(200)
        res.redirect('/list')
        console.log('{"ok":true,' + JSON.stringify(cloth_name) + ' }');

    })
});

// delete place
app.post('/place_delete', function (req, res, next) {
    var place_name = req.body.place_name;
    var new_places = New_places.find({ 'place_name': place_name })
    new_places.remove(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send('delete error')
            return;
        }
        res.status(200)
        res.redirect('/list2')
        console.log('{"ok":true,' + JSON.stringify(place_name) + ' }');
    })
});

function show_table(result, res) {
    res.writeHead(200);
    var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>지역</th><th>최저 기온</th><th>최고 기온</th><th>미세 먼지</th><th>강수량</th></tr>
                </thead>
                <tbody>
                `;
    for (var i = 0; i < result.length; i++) {
        template += `
        <tr>
            <td>${result[i]['location']}</td>
            <td>${result[i]['temp_min']}</td>
            <td>${result[i]['temp_max']}</td>
            <td>${result[i]['fine_dust']}</td>
            <td>${result[i]['prec']}</td>
        </tr>
        `;
    }
    template += `
                </tbody>
            </table>
        </body>
        </html>
    `;
    res.end(template);
}


/// functions for project
app.get("/select", (req, res) => {
    const result = connection.query("SELECT * FROM places;");

    if (result.length == 0) {
        res.send('{ "ok": false }');
    } else {
        res.writeHead(200);
        var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;" width="750px">
                <thead>
                    <tr><th>ID</th><th>Location</th><th>Name</th><th>Type</th></tr>
                </thead>
                <tbody>
                `;
        for (var i = 0; i < result.length; i++) {
            template += `
        <tr>
            <td>${result[i]['id']}</td>
            <td>${result[i]['location']}</td>
            <td>${result[i]['name']}</td>
            <td>${result[i]['type']}</td>
        </tr>
        `;
        }
        template += `
                </tbody>
            </table>
        </body>
        </html>
    `;
        res.end(template);
    }
});

app.get("/select_clothes", (req, res) => {
    const result = connection.query("SELECT * FROM clothes;");

    if (result.length == 0) {
        res.send('{ "ok": false }');
    } else {
        res.writeHead(200);
        var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>ID</th><th>Cloth Name</th><th>Category</th><th>Temp_min</th><th>Temp_max</th></tr>
                </thead>
                <tbody>
                `;
        for (var i = 0; i < result.length; i++) {
            template += `
        <tr>
            <td>${result[i]['id']}</td>
            <td>${result[i]['name']}</td>
            <td>${result[i]['category']}</td>
            <td>${result[i]['temp_min']}</td>
            <td>${result[i]['temp_max']}</td>
        </tr>
        `;
        }
        template += `
                </tbody>
            </table>
        </body>
        </html>
    `;
        res.end(template);
        console.log('{"ok": true,' + JSON.stringify(result) + ' }');
    }
});

app.get("/show_wt/:date", (req, res) => {
    const { date } = req.params;
    const result = connection.query("select * from weather WHERE date=?;", [date]);

    console.log(date)
    console.log(result)

    res.writeHead(200);
    var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Lato&family=Noto+Serif+KR:wght@600&display=swap');
            </style>
        </head>
        <body>
            <h2>🌞Today's Weather&nbsp;:&nbsp;&nbsp;${date}🌞</h2>
            <hr>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>지역</th><th>최저 기온</th><th>최고 기온</th><th>미세 먼지</th><th>강수량</th></tr>
                </thead>
                <tbody>
                `;
    for (var i = 0; i < result.length; i++) {
        template += `
        <tr>
            <td>${result[i]['location']}</td>
            <td>${result[i]['temp_min']}</td>
            <td>${result[i]['temp_max']}</td>
            <td>${result[i]['fine_dust']}</td>
            <td>${result[i]['prec']}</td>
        </tr>
        `;
    }
    template += `
                </tbody>
            </table>
        </body>
        </html>
    `;
    res.end(template);
});

app.post("/show_wt", (req, res) => {
    const { loc, date } = req.body;
    const result = connection.query("select * from weather WHERE location=? AND date=?;", [loc, date]);

    if (result.length == 0) {
        //console.log('{ "ok": false }');
        res.send('{ "ok": false }');
    } else {
        //console.log('{"ok":true,' + JSON.stringify(result) + ' }');
        res.send('{"ok":true,' + JSON.stringify(result) + ' }');
    }
});

app.get("/show_rec/:location", (req, res) => {
    const { location } = req.params;

    const result_place = connection.query(
        "SELECT w.location, w.date, p.name AS place_name FROM weather w JOIN places p ON w.location = p.location AND w.temp_min <= p.temp_min WHERE w.location=? AND w.date = '20230313'; ", [location]);

    const result_cloth = connection.query(
        "SELECT w.location, w.date, c.name AS cloth_name FROM clothes c JOIN weather w ON w.temp_max >= c.temp_max AND w.temp_min >= c.temp_min WHERE w.location=? AND w.date = '20230313'; ", [location]);

    const result_wt = connection.query("select * from weather WHERE location=? AND date='20230313';", [location]);

    if (result_place.length == 0 || result_cloth.length == 0 || result_wt.length == 0) {
        console.log('{ "ok": false }');
    } else {
        res.writeHead(200);
        var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <h2>20230313 ${location} 날씨 기반 추천 관광지</h2>
            <hr>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>지역</th><th>날짜</th><th>관광지 이름</th></tr>
                </thead>
                <tbody>
                `;
        for (var i = 0; i < result_place.length; i++) {
            template += `
        <tr>
            <td>${result_place[i]['location']}</td>
            <td>${result_place[i]['date']}</td>
            <td>${result_place[i]['place_name']}</td>
        </tr>
        `;
        }
        template += `
                </tbody>
            </table>

            <h2>20230313 ${location} 날씨 기반 추천 옷차림</h2>
            <hr>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>지역</th><th>날짜</th><th>추천 옷</th></tr>
                </thead>
                <tbody>
                `;
        for (var i = 0; i < result_cloth.length; i++) {
            template += `
        <tr>
            <td>${result_cloth[i]['location']}</td>
            <td>${result_cloth[i]['date']}</td>
            <td>${result_cloth[i]['cloth_name']}</td>
        </tr>
        `;
        }
        template += `
                </tbody>
            </table>

            <h2>20230313 ${location} 기상정보</h2>
            <hr>
            <table style="margin:auto; text-align:center;">
                <thead>
                    <tr><th>최저 기온</th><th>최고 기온</th><th>미세 먼지</th><th>강수량</th></tr>
                </thead>
                <tbody>
                `;
        for (var i = 0; i < result_wt.length; i++) {
            template += `
        <tr>
            <td>${result_wt[i]['temp_min']}</td>
            <td>${result_wt[i]['temp_max']}</td>
            <td>${result_wt[i]['fine_dust']}</td>
            <td>${result_wt[i]['prec']}</td>
        </tr>
        `;
        }
        template += `
        </body >
        </html >
            `;
        res.end(template);
        console.log('{"ok":true,' + JSON.stringify(result_place) + ' }');
        console.log('{"ok":true,' + JSON.stringify(result_cloth) + ' }');
        console.log('{"ok":true,' + JSON.stringify(result_wt) + ' }');
    }
});

app.post("/rec_place", (req, res) => {
    const { loc, date } = req.body;
    const result = connection.query(
        "SELECT w.location, w.date, p.name AS place_name FROM weather w JOIN places p ON w.location = p.location AND w.temp_min <= p.temp_min WHERE w.location=? AND w.date=?;", [loc, date]);
    console.log('{"ok":true,' + JSON.stringify(result) + ' }');

    if (result.length == 0) {
        res.send('{ "ok": false }');
    } else {
        res.send('{"ok": true,' + JSON.stringify(result) + ' }');
    }
});


app.get("/rec_cloth", (req, res) => {
    const result = connection.query(
        "SELECT w.location, w.date, c.name AS cloth_name FROM clothes c JOIN weather w ON w.temp_max >= c.temp_max AND w.temp_min >= c.temp_min WHERE w.location = '대구' AND w.date = '20230329'; ");
    console.log(result);
    res.send(result);
});

app.post("/rec_cloth", (req, res) => {
    const { loc, date } = req.body;
    const result = connection.query(
        "SELECT w.location, w.date, c.name AS cloth_name FROM clothes c JOIN weather w ON w.temp_max >= c.temp_max AND w.temp_min >= c.temp_min WHERE w.location = ? AND w.date = ?;", [loc, date]);
    console.log(result);
    res.send(result);
});


app.post("/find_my_cloth", (req, res) => {
    const { now_temp, cloth_category } = req.body;
    const clothes = connection.query("select name, temp_min, temp_max from clothes where category=?", [cloth_category]);
    const mintemp = [];
    const maxtemp = [];
    const result = [];

    console.log(clothes)

    Array.from(clothes).forEach((clothing) => {
        mintemp.push(clothing.temp_min);
        maxtemp.push(clothing.temp_max);
    });

    if (now_temp.length == 0 || cloth_category.length == 0) {
        res.send(
            `<script>
            alert('현재 온도와 원하시는 옷 카테고리를 모두 입력해주세요!');
            </script > `
        );
        return;
    } else {
        for (var i = 0; i < clothes.length; i++) {
            if ((maxtemp[i] >= now_temp) && (mintemp[i] <= now_temp)) {
                result.push(clothes[i].name);
            }
        }
        res.writeHead(200);
        var template = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="/table.css">
        </head>
        <body>
            <table style="margin:auto; text-align:center;" width="300px">
                <thead>
                    <tr><th>Recommand clothes for you</th></tr>
                </thead>
                <tbody>
                `;
        for (var i = 0; i < clothes.length; i++) {
            template += `
        <tr>
            <td>${clothes[i]['name']}</td>
        </tr>
        `;
        }
        template += `
                </tbody>
            </table>
        </body>
        </html>
    `;
        res.end(template);
    }
});


module.exports = app;