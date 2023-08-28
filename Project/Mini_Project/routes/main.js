const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: '../../.env' });

var connection = new mysql({
   host: process.env.host,
   user: process.env.user,
   password: process.env.password,
   database: process.env.database,
});

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/select', (req, res) => {
   const result = connection.query('select * from users');
   console.log(result);
   res.send(result);
});

app.post('/select', (req, res) => {
   const result = connection.query('select * from users');
   console.log(result);
   res.send(result);
});

app.get('/selectQuery', (req, res) => {
   const id = req.query.id;
   const result = connection.query('SELECT * FROM users where id=?', [id]);
   console.log(result);
   res.send(result);
});

app.post('/selectQuery', (req, res) => {
   const id = req.body.id;
   const result = connection.query('SELECT * FROM users where id=?', [id]);
   console.log(result);
   res.send(result);
});

app.post('/insert', (req, res) => {
   const { id, name, gender, age, location } = req.body;
   const result = connection.query('insert into users values(?, ?, ?, ?, ?)', [id, name, gender, age, location]);
   console.log(result);
   res.redirect('/selectQuery?id=' + req.body.id);
});

app.post('/update', (req, res) => {
   const { name, gender, age, location, id } = req.body;
   const result = connection.query('update users set username=?, gender=?, age=?, location=? where id=?', [
      name,
      gender,
      age,
      location,
      id,
   ]);
   console.log(result);
   res.redirect('/selectQuery?id=' + req.body.id);
});

app.post('/delete', (req, res) => {
   const id = req.body.id;
   const result = connection.query('delete from users where id=?', [id]);
   console.log(result);
   res.redirect('/select');
});

module.exports = app;
