// 导入express
const express = require('express')
// 导入mysql
const mysql = require('mysql') 
// 导入cors 
const cors = require('cors') 
const db = mysql.createPool({       // 建立与 MySQL 数据库的连接关系
    host: '127.0.0.1',                // 数据库的 IP 地址
    user: 'root',                     // 登录数据库的账号
    password: '123456',               // 登录数据库的密码
    database: 'summer',                 // 指定要操作哪个数据库
})
// 创建服务和端口
const app = express()
const port = 3000
// 使用中间件解决跨域问题和body参数传递问题
app.use(cors())
app.use(express.urlencoded({ extended: false }))
// 创建路由：前端通过xxx方式访问xxx地址。
app.get('/poem',(req,res)=>{
    // 查询 summerWeb 表中所有的数据
    db.query('select * from summerWeb', (err, results) => {
        if (err) return console.log(err.message)
        // 查询成功
        // 注意：如果执行的是 select 查询语句，则执行的结果是数组
        res.send(results)
    })
})

app.post('/poem',(req,res)=>{
    //接受传递过来的数据 
    let poem = req.body.poem
    // 操作数据库
    // 1. 将需要往数据库插入的数据，包装成对象 。重点：键名和数据库表中的字段保持一直。
    let poemData = {content: poem}
    //2. 编写sql语句
    let sqlStr = 'insert into summerWeb set ?'
    //3. 执行 SQL 语句
    db.query(sqlStr, poemData, (err, results) => {
        if (err) return console.log(err.message,'数据库插入数据失败')
        if (results.affectedRows === 1) {
            res.send(`存储成功poem`)
        }
    })
})
// 启动服务。监听端口
app.listen(port, () => {
    console.log(`server...is...running...http://localhost:${port}`)
})
