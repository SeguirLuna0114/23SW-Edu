const express = require('express');
const bodyParser = require('body-parser');
// const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

const morgan = require('morgan');
const fs = require('fs');
const path = require('path');
const mongoClient = require('mongodb').MongoClient;

const app = express();
app.set('port', process.env.PORT || 5000);
app.use(morgan('dev'));

var db;
var databaseUrl = "mongodb://192.168.1.189:27017";
app.get('/', (req, res) => {
    res.redirect('login.html');
})

const axios = require('axios'); //http요청을 보내고 응답을 받는 라이브러리

// carwash_list로 get요청을 보내고, 요청이 성공한다면 반환된 데이터를 출력
axios.get('http://192.168.1.189:8000/carwash_list')
    .then(response => {
        console.log(response.data); //서버응답 출력
        // const docs = response.data.carwash;
        const data = response.data;
        const docs = data.carwash;
        console.log(JSON.stringify(docs));//docs를 정의함
        for (let i = 0; i < docs.length; i++) {
            console.log(JSON.stringify({company: docs[i].company}));
            console.log(JSON.stringify({state: docs[i].state}));
            console.log(JSON.stringify({industry: docs[i].industry}));
            console.log(JSON.stringify({type: docs[i].type}));
            console.log(JSON.stringify({off: docs[i].off}));
            console.log(JSON.stringify({dayopen: docs[i].dayopen}));
            console.log(JSON.stringify({dayclose: docs[i].dayclose}));
            console.log(JSON.stringify({TelNo: docs[i].TelNo}));
            console.log(JSON.stringify({lapti: docs[i].lapti}));
            console.log(JSON.stringify({longit: docs[i].longit}));
            console.log(JSON.stringify({address: docs[i].address}));
        }
    })
    .catch(err => {
        console.error(err);
})

// carwash_get_state로 get요청을 보내고 반환된 데이터를 출력
axios.get('http://192.168.1.189.:8000/carwash_get_state?state=송파구')
    .then(response => {
        const docs = response.data.carwash;
        console.log(docs);//docs를 정의함
        for (let i = 0; i < docs.length; i++) {
            console.log(`company: ${docs[i].company}`);
            console.log(`state: ${docs[i].state}`);
            console.log(`industry: ${docs[i].industry}`);
            console.log(`type: ${docs[i].type}`);
            console.log(`off: ${docs[i].off}`);
            console.log(`dayopen: ${docs[i].dayopen}`);
            console.log(`dayclose: ${docs[i].dayclose}`);
            console.log(`TelNo: ${docs[i].TelNo}`);
            console.log(`lapti: ${docs[i].lapti }`);
            console.log(`longit: ${docs[i].longit}`);
            console.log(`address: ${docs[i].address}`);
        }
    })
    .catch(err => {
        console.error(err);
})

//carwash_get_state로 get요청을 보내고 반환된 데이터를 출력
axios.get('192.168.1.189.:8000/carwash_get_state&type?state=송파구&type=손세차')
    .then(response => {
        const docs = response.data.carwash;
        console.log(docs);//docs를 정의함
        for (let i = 0; i < docs.length; i++) {
            console.log(`company: ${docs[i].company}`);
            console.log(`state: ${docs[i].state}`);
            console.log(`industry: ${docs[i].industry}`);
            console.log(`type: ${docs[i].type}`);
            console.log(`off: ${docs[i].off}`);
            console.log(`dayopen: ${docs[i].dayopen}`);
            console.log(`dayclose: ${docs[i].dayclose}`);
            console.log(`TelNo: ${docs[i].TelNo}`);
            console.log(`lapti: ${docs[i].lapti }`);
            console.log(`longit: ${docs[i].longit}`);
            console.log(`address: ${docs[i].address}`);
        }
    })
    .catch(err => {
        console.error(err);
})


axios.post('http://192.168.1.189:8000/carwash_insert')
    .then(response => {
        const docs = response.data.carwash;
        console.log(docs);//docs를 정의함
        for (let i = 0; i < docs.length; i++) {
            console.log(`company: ${docs[i].company}`);
            console.log(`state: ${docs[i].state}`);
            console.log(`industry: ${docs[i].industry}`);
            console.log(`type: ${docs[i].type}`);
            console.log(`off: ${docs[i].off}`);
            console.log(`dayopen: ${docs[i].dayopen}`);
            console.log(`dayclose: ${docs[i].dayclose}`);
            console.log(`TelNo: ${docs[i].TelNo}`);
            console.log(`lapti: ${docs[i].lapti }`);
            console.log(`longit: ${docs[i].longit}`);
            console.log(`address: ${docs[i].address}`);
        }
    })
    .catch(err => {
        console.error(err);
})


// // request O, query X
// app.get('/select', (req, res) => {
//     const result = connection.query('select * from user');
//     console.log(result);
//     // res.send(result);
//     res.writeHead(200); //200=성공했다는 뜻
//     if (result.length == 0) {
//         var template = ` 
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//             <h3>데이터가 존재하지 않습니다.</h3>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     } else {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//         <table border="1" style="margin:auto;">
//         <thead>
//             <tr><th>User ID</th><th>Password</th></tr>
//         </thead>
//         <tbody>
//         `;
//         for (var i = 0; i < result.length; i++) { //result의 length만큼 반복할 것
//             template += `
//         <tr>
//             <td>${result[i]['userid']}</td>
//             <td>${result[i]['passwd']}</td>
//         </tr>
//         `;
//         }
//         template += `
//         </tbody>
//         </table>
//         </body>
//         </html>
//         `;
//         res.end(template); //'end'처리함
//     }
// })

// // request O, query X
// app.post('/select', (req, res) => { //select는 parameter가 없기에, parameter검사 불필요
//     const result = connection.query('select * from user');
//     console.log(result);
//     // res.send(result);
//     res.writeHead(200);
//     if (result.length == 0) {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//             <h3>데이터가 존재하지 않습니다.</h3>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     } else {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//         <table border="1" style="margin:auto;">
//         <thead>
//             <tr><th>User ID</th><th>Password</th></tr>
//         </thead>
//         <tbody>
//         `;
//         for (var i = 0; i < result.length; i++) {
//             template += `
//         <tr>
//             <td>${result[i]['userid']}</td>
//             <td>${result[i]['passwd']}</td>
//         </tr>
//         `;
//         }
//         template += `
//         </tbody>
//         </table>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     }
// })

// // request O, query O
// app.get('/selectQuery', (req, res) => {
//     const id = req.query.id;
//     const result = connection.query("select * from user where userid=?", [id]);
//     console.log(result);
//     // res.send(result);
//     res.writeHead(200);
//     if (result.length == 0) {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//             <h3>데이터가 존재하지 않습니다.</h3>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     } else {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//         <table border="1" style="margin:auto;">
//         <thead>
//             <tr><th>User ID</th><th>Password</th></tr>
//         </thead>
//         <tbody>
//         `;
//         for (var i = 0; i < result.length; i++) {
//             template += `
//         <tr>
//             <td>${result[i]['userid']}</td>
//             <td>${result[i]['passwd']}</td>
//         </tr>
//         `;
//         }
//         template += `
//         </tbody>
//         </table>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     }
// })

// // request O, query O
// app.post('/selectQuery', (req, res) => {
//     const id = req.body.id;
//     // console.log(req.body);
//     const result = connection.query("select * from user where userid=?", [id]);
//     console.log(result);
//     // res.send(result);
//     res.writeHead(200);
//     if (result.length == 0) {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//             <h3>데이터가 존재하지 않습니다.</h3>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     } else {
//         var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Result</title>
//             <meta charset="utf-8">
//             <link type="text/css" rel="stylesheet" href="mystyle.css" />
//         </head>
//         <body>
//         <table border="1" style="margin:auto;">
//         <thead>
//             <tr><th>User ID</th><th>Password</th></tr>
//         </thead>
//         <tbody>
//         `;
//         for (var i = 0; i < result.length; i++) {
//             template += `
//         <tr>
//             <td>${result[i]['userid']}</td>
//             <td>${result[i]['passwd']}</td>
//         </tr>
//         `;
//         }
//         template += `
//         </tbody>
//         </table>
//         </body>
//         </html>
//         `;
//         res.end(template);
//     }
// })

// // request O, query O
// app.post('/insert', (req, res) => {
//     const { id, pw } = req.body;
//     const result = connection.query("insert into user values (?, ?)", [id, pw]);
//     console.log(result);
//     res.redirect('/selectQuery?id=' + req.body.id);
// })

// // request O, query O
// app.post('/update', (req, res) => {
//     const { id, pw } = req.body;
//     const result = connection.query("update user set passwd=? where userid=?", [pw, id]);
//     console.log(result);
//     res.redirect('/selectQuery?id=' + req.body.id);
// })

// // request O, query O
// app.post('/delete', (req, res) => {
//     const id = req.body.id;
//     const result = connection.query("delete from user where userid=?", [id]);
//     console.log(result);
//     res.redirect('/select');
// })

module.exports = app;
