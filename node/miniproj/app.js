const express = require('express'); //node.js 웹 애플리케이션 프레임워크
const morgan = require('morgan'); //request와 resopnse사이 공통기능 수행 소프트웨어. 요청의 본문을 지정 형태로 파싱해주는 미들웨어
const path = require('path')
const app = express(); //express 웹프레임워크를 이용한 서버 띄우기
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser')
const router = express.Router()

app.set('port', process.env.PORT || 8000)
app.use(morgan('dev'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(express.static(path.join(__dirname, 'public')))

// mongoose configuration
const mongoose = require("mongoose")
mongoose.connect("mongodb://192.168.1.189:27017/test")

var main = require('./routes/main.js')
app.use('/', main)

app.listen(app.get('port'), () => {
    console.log('8000 Port : Server Started...')
});