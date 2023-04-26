const express = require("express")
const app = express.Router()
const mongoose = require("mongoose")
// const async = require("async")

//define schema
var carwashSchema = mongoose.Schema({
    company: String,
    state: String,
    industry: String,
    type: String,
    address: String,
    off: String,
    dayopen: String,
    dayclose: String,
    holopen: String,
    holclose: String,
    TelNo: String,
    location: {
        type: {
            type: String,
            enum: ['Point'],
            required: true
        },
        coordinates: {
            type: [Number],
            required: true
        }
    }
}, {
    versionKey: false
});

//create model with mongodb collection and schema
var Carwash = mongoose.model('Carwash', carwashSchema);

app.get('/', (req, res) => {
    res.send("Web server Started~!!");
})

app.get('/hello', function (req, res) {
    res.send("Hello World~!!")
})

// select
app.get('/select', function (req, res, next) {
    var company = req.query.company;
    var state = req.query.state;
    var industry = req.query.industry;
    var type = req.query.type;

    var off = req.query.off;
    var dayopen = req.query.dayopen;
    var dayclose = req.query.dayclose;
    var holopen = req.query.holopen;
    var holclose = req.query.holclose;
    var TelNo = req.query.TelNo;
    var lapti = req.query.location.coordinates[1];
    var longit = req.query.location.coordinates[0];
    var address = req.query.address;
    var carwash = new Carwash({ 'company': company, 'state': state, 'industry': industry, 'type': type, 'off': off, 'dayopen': dayopen, 'dayclose': dayclose, 'holopen': holopen, 'holclose': holclose, 'TelNo': TelNo, 'lapti': lapti, 'longit': longit, 'address': address, })
    carwash.findOne({ 'state': "송파구" }, function (err, doc) {
        if (err) console.log(err)
        // res.send(doc)
        res.send(JSON.stringify({ "ok": true, "carwash": doc }));
            console.log(JSON.stringify({ "ok": true, "carwash": doc }));
    })
})

// list
app.get('/list', function (req, res, next) {
    Carwash.find({}, function (err, docs) {
        if (err) console.log('err')
        // res.send(docs)
        res.send(JSON.stringify({ "ok": true, "carwash_list": docs }));
            console.log(JSON.stringify({ "ok": true, "carwash_": docs }));
    })
})

// insert
app.post('/insert', function (req, res, next) {
    var company = req.body.company;
    var state = req.body.state;
    var industry = req.body.industry;
    var type = req.body.type;

    var off = req.body.off;
    var dayopen = req.body.dayopen;
    var dayclose = req.body.dayclose;
    var holopen = req.body.holopen;
    var holclose = req.body.holclose;
    var TelNo = req.body.TelNo;
    var lapti = req.body.location.coordinates[1];
    var longit = req.body.location.coordinates[0];
    var address = req.body.address;
    var carwash = new Carwash({ 'company': company, 'state': state, 'industry': industry, 'type': type, 'off': off, 'dayopen': dayopen, 'dayclose': dayclose, 'holopen': holopen, 'holclose': holclose, 'TelNo': TelNo, 'lapti': lapti, 'longit': longit, 'address': address, })

    carwash.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('insert error')
                res.send('{ "ok": false }');
                console.log('{ "ok": false }');
                return;
            }
            res.status(200)
            res.send('{ "ok": true, "carwash_id":' + JSON.stringify(carwash) + '}');
            console.log('{ "ok": true, "carwash_id":' + JSON.stringify(carwash) + '}');
        })
})

// update
app.post('/update', function (req, res, next) {
    var company = req.body.company;
    var state = req.body.state;
    var industry = req.body.industry;
    var type = req.body.type;
    var location = req.body.location;
    var off = req.body.off;
    var dayopen = req.body.dayopen;
    var dayclose = req.body.dayclose;
    var holopen = req.body.holopen;
    var holclose = req.body.holclose;
    var TelNo = req.body.TelNo;
    var lapti = req.body.location.coordinates[1];
    var longit = req.body.location.coordinates[0];

    Carwash.findOne({ 'company': company }, function (err, carwash) {
        if (err) {
            console.log('err')
            res.status(500).send('update error')
            return;
        }
        carwash.state = state;
        carwash.industry = industry;
        carwash.type = type;
        carwash.location = location;
        carwash.off = off;
        carwash.dayopen = dayopen;
        carwash.dayclose = dayclose;
        carwash.holopen = holopen;
        carwash.holclose = holclose;
        carwash.TelNo = TelNo;
        carwash.lapti = lapti;
        carwash.longit = longit;

        carwash.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('update error')
                return;
            }
            res.status(200).send("Updated")
        })
    })
})


// delete
app.post('/delete', function (req, res, next) {
    var company = req.body.company;
    var carwash = Carwash.find({ 'company': company })
    carwash.deleteOne(function (err) {
        if (err) {
            console.log('err')
            res.status(500).send('delete error')
            return;
        }
        res.status(200).send("Removed")
    })
})

function show_Position(result, res) {
    res.writeHead(200);
    var template =`
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>getCurrentPosition()로 현재 위치 파악</title>
    </head>
    <body>
    <h3>getCurrentPosition()로 현재 위치 파악</h3>
    <hr>
    <div id="msg">이곳에 위치 정보 출력</div>
    <script>
    if(navigator.geolocation)
        navigator.geolocation.getCurrentPosition(success); 
    else
        alert("지원하지 않음");
   
    function success(position) {
        let lat = position.coords.latitude; // 위도
        let lon = position.coords.longitude; // 경도
        let acc = position.coords.accuracy; // 정확도

        lat = lat.toPrecision(6); lon = lon.toPrecision(6);
        let now = new Date(position.timestamp);
        let text = "현재 시간 " + now.toUTCString() + "<br>";
        text += "현재 위치 (위도 " + lat + "°, 경도 " + lon + "°)<br>";
        text += "정확도 " + acc + "m<br>";
        document.getElementById("msg").innerHTML = text;
    }
    </script>
    </body>
    </html>
    `;
    res.end(template);
}

function show_map(result, res) {
    res.writeHead(200);
    var template =`
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>현재 위치와 지도 출력</title>
    </head>
    <body>
    <h3>현재 위치와 지도 출력</h3>
    <hr>
    <div id="msg">이곳에 위치 정보 출력</div>
    <iframe id="map" width="425" height="350" frameborder="0" scrolling="no" marginheight="0"
    marginwidth="0" ></iframe><br/>
    <a id="bigmaplink" target="_blank">새 창에 큰 지도 보기</a>
    <script>
    if(navigator.geolocation)
    navigator.geolocation.getCurrentPosition(success);
    else
    alert("지원하지 않음");
    function success(position) {
        let lat = position.coords.latitude; 
        let lon = position.coords.longitude; 
        let acc = position.coords.accuracy; 
        
        lat = lat.toPrecision(6); lon = lon.toPrecision(6);
        let now = new Date(position.timestamp);
        let text = "현재 시간 " + now.toUTCString() + "<br>";
        text += "현재 위치 (위도 " + lat + "°, 경도 " + lon + "°)<br>";
        text += "정확도 " + acc + "m<br>";
        document.getElementById("msg").innerHTML = text;
        let map = document.getElementById("map");
        map.src ="https://www.openstreetmap.org/export/embed.html?bbox=" +
        (parseFloat(lon)-0.01) + "%2C" + (parseFloat(lat)-0.01) + "%2C" +
        (parseFloat(lon)+0.01) + "%2C" + (parseFloat(lat) + 0.01);
        
        let maplink = document.getElementById("bigmaplink");
        let zoom = 15; 
        maplink.href = "https://www.openstreetmap.org/#map=" + zoom + "/" + lat + "/" + lon;
        }
        </script>
        </body>
        </html>
        `;
        res.end(template);
}

module.exports = app;