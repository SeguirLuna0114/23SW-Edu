const express = require("express")
const app = express.Router()
const mongoose = require("mongoose")
const async = require("async")

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

// select
app.get('/select', function (req, res, next) {
    var state = req.query.input
    Carwash.find({ 'state': state },{ '_id': 0 })
            .select('company type location off Telno')
            .exec(function (err, doc) {
            if (err) console.log('err')
            res.send(doc)
            })
}); // where state = req.query.input.state

module.exports = app;