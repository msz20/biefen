const express = require('express')
const mysql = require('mysql')
const cors = require('cors')
const db = mysql.createPool({
    host: '127.0.0.1',
    user: 'root',
    password: '20110214msz',
    database: 'summer123',
})
const app = express()
const port = 3000
app.use(cors())
// app.use(express.urlencoded({ extended: false }))

app.use(express.urlencoded({ extended: false }))
app.get('/poem', (req, res) => {
    res.send('getOK ')
})

app.post('/poem', (req, res) => {

    let poem = req.body.poem
    console.log('req.body',req.body);
    console.log('poem值:',poem);
    let poemData = { content: poem }
    let sqlStr = 'insert into summer set ?'
    db.query(sqlStr, poemData, (err, results) => {
        if (err) return console.log(err.message, '插入失败')
        if (results.affectedRows === 1) {
            res.send(`OK`)
        }
    })
})
app.listen(port, () => {
    console.log(`sever...is...OK...http://localhost/${port}`)
})
