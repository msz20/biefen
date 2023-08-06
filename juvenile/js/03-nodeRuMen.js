//创建web服务器程序用来给网页访问。借助express包
const express = require('express')

const mysql = require('mysql')      // 1. 导入 mysql 模块

const db = mysql.createPool({       // 2. 建立与 MySQL 数据库的连接关系
    host: '127.0.0.1',                // 数据库的 IP 地址
    user: 'root',                     // 登录数据库的账号
    password: '123456',               // 登录数据库的密码
    database: 'summer',                 // 指定要操作哪个数据库
})



const app = express()
const port = 3000
// 获取post请求提交的数据
app.use(express.urlencoded({ extended: false }))

app.get('/hello', (req, res) => {
    // 解决跨域问题
    res.setHeader('Access-Control-Allow-Origin', '*')
    res.send('你好啊客户端。我是服务端')
})

app.get('/data', (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*')
    

    // 操作数据库 查询
    // 查询 users 表中所有的数据
    db.query('select * from summerWeb', (err, results) => {
        if (err) return console.log(err.message)
        // 查询成功
        // 注意：如果执行的是 select 查询语句，则执行的结果是数组

        res.send(results)
    })
    
})
app.post('/data', (req, res) => {
    // 解决跨域问题
    res.setHeader('Access-Control-Allow-Origin', '*')

    let textCon = req.body.textCon

    // 操作数据库
    let dataObj = { content: textCon }
    let sqlStr = 'insert into summerWeb set ?'
    // 执行 SQL 语句
    db.query(sqlStr, dataObj, (err, results) => {
        if (err) return console.log(err.message)
        if (results.affectedRows === 1) {
            res.send(`存储成功${textCon}`)
        }
    })

})


app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
