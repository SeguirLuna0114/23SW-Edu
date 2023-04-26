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
    location: String,
    off: String,
    dayopen: String,
    dayclose: String,
    holopen: String,
    holclose: String,
    TelNo: String, 
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

// select
app.get('/select', function (req, res, next) {
    var state = req.query.input;
    Carwash.find({ 'state': state },{ '_id': 0 })
            .select('company type location off TelNo')
            .exec(function (err, doc) {
              if (err) {
                console.log(err);  // 에러 발생 시 로그 출력
                return next(err);  // 에러를 전달하여 다음 미들웨어로 이동
              }
  
              if (!doc) {
                return res.send('No data found');  // doc 값이 없으면 응답 보내기
              }
  
              res.send(doc);
            });
});

// insert
app.post('/insert', function (req, res, next) {
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
    var lapti = req.body.lapti;
    var longit = req.body.longit;
    var carwash = new Carwash({ 'company': company, 'state': state, 'industry': industry, 'type': type, 'location': location, 'off': off, 'dayopen': dayopen, 'dayclose': dayclose, 'holopen': holopen, 'holclose': holclose, 'TelNo': TelNo, 'lapti': lapti, 'longit': longit })

    carwash.save(function (err, silence) {
            if (err) {
                console.log('err')
                res.status(500).send('insert error')
                return;
            }
            res.status(200).send("Inserted")
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
    var lapti = req.body.lapti;
    var longit = req.body.longit;

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

module.exports = app;