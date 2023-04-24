var mysql = require('sync-mysql'); //설치된 sync-mysql 모듈 추가
const env = require('dotenv').config({ path: "../../.env" });

var connection = new mysql({ //기존에 만들어둔 mysql 데이터베이스에 접속
    host: process.env.host, //mysql 주소
    user: process.env.user, //user
    port: process.env.port,
    password: process.env.password, //비밀번호
    database: process.env.database //데이터베이스 이름
})

let result = connection.query('select * from st_info'); //'st_info'테이블의 모든 데이터를 가져오는 코드
console.log(result); //st_info db를 출력

// make insert data
let data ={
    st_id: "202399",
    name: "Moon",
    dept: "Computer"
}

// inserted data's id
let insertId = data.st_id;

// insert query
result = connection.query("insert into st_info values (?, ?, ?)", [insertId, data.name, data.dept]); //connection.query의 실행결과로 받는 result에 insert 쿼리의 실행결과 정보를 받게됨
console.log("data is Inserted~!!");

// select query for inserted data
result = connection.query('select * from st_info where st_id =?', [insertId]); //connection.query(sql문, [values])
console.log(result);

// update query
result = connection.query("update st_info set dept=? where st_id = ? ", ["Game", insertId]);
console.log("data is Updated~!!");

// select query of inserted data
result = connection.query('select * from st_info where st_id = ?', [insertId]);
console.log(result);

// delete row
result = connection.query("delete from st_info where st_id = ?", [insertId]);
console.log(result);

// select query all data
result = connection.query("select * from st_info");
console.log(result);
