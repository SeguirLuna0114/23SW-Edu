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
    off: String,
    dayopen: String,
    dayclose: String,
    holopen: String,
    holclose: String,
    TelNo: String,
    lapti: String,
    longit: String,
    address: String
}, {
    versionKey: false
});

//create model with mongodb collection and schema
var Carwash = mongoose.model('carwashes', carwashSchema);

app.get('/', (req, res) => {
    res.send("Web server Started~!!");
})

app.get('/hello', function (req, res) {
    res.send("Hello World~!!")
})

// carwash_list
app.get('/carwash_list', function (req, res, next) {
    Carwash.find({}, function (err, docs) {
        if (err) {
            console.error(err);
            return res.status(500).json({ ok: false, db: "mongoose", service: "carwash_list", error: err });
          }
          if (docs.length > 0) {
            res.status(200).json({ ok: true, carwash: docs });
          } else {
            res.status(404).json({ ok: false, db: "mongoose", service: "carwash_list", message: "No carwashes found" });
          }
    })
})

//carwash_get_state
app.get('/carwash_get_state', function (req, res, next) {
    var state = req.query.state;
    Carwash.findOne({ 'state': state }, { '_id': 0 }, function (err, docs) {
      if (err) {
        console.error(err);
        return res.status(500).json({ ok: false, db: "mongoose", service: "carwash_get_state", error: err });
      }
      if (!docs) { // handle null value of carwash
        return res.status(404).json({ ok: false, db: "mongoose", service: "carwash_get_state", message: "No carwash found" });
      }
      res.status(200).json({ ok: true, carwash: docs });
    })
})

//carwash_get_state&type
app.get('/carwash_get_state&type', function (req, res, next) {
    var state = req.query.state;
    var type = req.query.type;
    Carwash.findOne({ 'state': state, 'type': type }, function (err, docs) {
      if (err) {
        console.error(err);
        return res.status(500).json({ ok: false, db: "mongoose", service: "carwash_get_state & type", error: err });
      }
      if (!docs) { // handle null value of carwash
        return res.status(404).json({ ok: false, db: "mongoose", service: "carwash_get_state & type", message: "No carwash found" });
      }
      res.status(200).json({ ok: true, carwash: docs });
    })
})

// carwash_insert
app.post('/carwash_insert', function (req, res, next) {
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
    var lapti = req.body.lapti;
    var longit = req.body.longit;
    var address = req.body.address;
  
    var carwash = new Carwash({
      'company': company,
      'state': state,
      'industry': industry,
      'type': type,
      'off': off,
      'dayopen': dayopen,
      'dayclose': dayclose,
      'holopen': holopen,
      'holclose': holclose,
      'TelNo': TelNo,
      'lapti': lapti,
      'longit': longit,
      'address': address
    });
  
    carwash.save(function (err, doc) {
      if (err) {
        console.error(err);
        return res.status(500).json({
          ok: false,
          db: "mongoose",
          service: "carwash_insert",
          error: err
        });
      }
      res.status(200).json({ ok: true, carwash: doc });
    });
});

// carwash_update
app.post('/carwash_update', function (req, res, next) {
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
    var lapti = req.body.lapti;
    var longit = req.body.longit;
    var address = req.body.address;
  
    Carwash.findOne({ 'company': company }, function (err, docs) {
      if (err) {
        console.error(err);
        res.status(500).json({
          ok: false,
          db: "mongoose",
          service: "carwash_update",
          error: err
        })
        return;
      }
      if (!docs) {
        return res.status(404).json({
          ok: false,
          db: "mongoose",
          service: "carwash_update",
          message: "No carwash found"
        })
      }
  
      docs.state = state;
      docs.industry = industry;
      docs.type = type;
      docs.off = off;
      docs.dayopen = dayopen;
      docs.dayclose = dayclose;
      docs.holopen = holopen;
      docs.holclose = holclose;
      docs.TelNo = TelNo;
      docs.lapti = lapti;
      docs.longit = longit;
      docs.address = address;

      docs.save(function (err, updatedDoc) {
        if (err) {
          console.error(err);
          return res.status(500).json({
            ok: false,
            db: "mongoose",
            service: "carwash_update",
            error: err
          })
        }
        res.status(200).json({
          ok: true,
          db: "mongoose",
          service: "carwash_update",
          message: "Carwash updated successfully",
          updated_carwash: updatedDoc
        })
      })
    })
})

// carwash_delete
app.post('/carwash_delete', function (req, res, next) {
    var company = req.body.company;
    var del = Carwash.find({ 'company': company })
    del.deleteOne(function (err) {
        if (err) {
            console.error(err);
            return res.status(500).json({
              ok: false,
              db: "mongoose",
              service: "carwash_delete error",
              error: err
        })
        }
        res.status(200).json({ ok: true, company: company + " removed" });
    })
})

module.exports = app;