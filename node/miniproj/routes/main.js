const express = require('express'); //node.js 웹 애플리케이션 프레임워크
const morgan = require('morgan'); //request와 resopnse사이 공통기능 수행 소프트웨어. 요청의 본문을 지정 형태로 파싱해주는 미들웨어
const fs = require('fs'); //파일시스템 사용을 위한 패키지
const path = require('path');
const mongoose = require("mongoose");
const mongoClient = require('mongodb').MongoClient;

const app = express(); //express 웹프레임워크를 이용한 서버 띄우기
app.set('port', process.env.Port || 8000);
app.use(morgan('dev'));

// var db;
// var databaseUrl = "mongodb://192.168.1.189:27017";

//define schema
var carwashSchema = mongoose.Schema({
    company: String,
    state: String,
    industry: String,
    type: String,
    location: String,
    off: String,
    dayopen: String,
    dayclose: String,
    holopen: String,
    holclose: String,
    Telno: String, 
    lapti: Number,
    longit: Number
}, {
    versionKey: false
})

//create model with mongodb collection and schema
var Carwash = mongoose.model('carwash', carwashSchema);

app.get('/', (req, res) => {
    res.send("Web server Started~!!");
})

app.get('/hello', function (req, res) {
    res.send("Hello World~!!")
})

// // select
// app.get('/select', function (req, res, next) {
//     var state = req.query.input
//     Carwash.find({ 'state': state },{ '_id': 0 })
//             .select('company type location off Telno')
//             .exec(function (err, doc) {
//             if (err) console.log('err')
//             res.send(doc)
//             })
// }); // where state = req.query.input.state


module.exports = app;