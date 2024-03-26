const express = require('express');
const {spawn} = require('child_process');
const iconv = require('iconv-lite');
const app = express();
const port = 8000;
let rs;

app.get("/",  (req, res) => {
    // 파이썬 코드 실행
    const pythonProcess =  spawn('python', ['menu.py']);

    // 파이썬 코드 출력 받아옴
    let pythonOutput = '';
    pythonProcess.stdout.on('data', (data) => {
        pythonOutput += data.toString('utf8');
    });

    // 파이썬 코드 실행 완료되면 결과를 웹에 뿌려줌

    pythonProcess.on('close', (code) => {
        result = pythonOutput.replace("b'", "");
        result = result.replace("'", "");
        let bytes = Buffer.from(result, 'base64');
        bytes = bytes.toString('utf8');

        console.log(bytes)
        res.send(bytes)

        // result = "7JWI64WV7ZWY7IS47JqU";
    })
})

app.listen(port, () => {
    console.log(`listening localhost:${port}`)
})