// chrome --headless --remote-debugging-port=9222 https://chromium.org
// chrome --headless --disable-gpu --dump-dom https://www.chromestatus.com/
// chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/
// chrome --headless --disable-gpu --screenshot https://www.chromestatus.com/
// chrome --headless --disable-gpu --screenshot --window-size=1280,1696 https://www.chromestatus.com/
// chrome --headless --disable-gpu --screenshot --window-size=412,732 https://www.chromestatus.com/

// alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
// alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
// alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"

// npm i --save puppeteer --ignore-scripts  跳过安装各种依赖包

const puppeteer = require('puppeteer');

var arguments = process.argv.splice(2);
var port = (arguments.length > 1 && /^[6-9][0-9]{3}$/.test(arguments[1]) ) ? arguments[1] : 8888;

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'd:/chrome-win32/chrome.exe',
        headless: true,
        slowMo: 200,
        ignoreHTTPSErrors: true,
        timeout: 30000
    });
    const page = await browser.newPage();
    await page.setViewport({width: 800, height: 600, isMobile: true});
    await page.setUserAgent('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36');
    await page.goto('http://music.163.com/');

    const dimensions = await page.evaluate(() => { // 通过evaluate执行页面js
        return {
            width: document.documentElement.clientWidth, // 页面宽度
            height: document.documentElement.clientHeight, // 页面高度
            deviceScaleFactor: window.devicePixelRatio // 设备像素比
        };
    });

    console.log('Dimensions:', dimensions);

    //await page.screenshot({path: 'music.png'});
    //await page.pdf({path: 'music.pdf', format: 'A4'});
    await browser.close();
})();


/* puppeteer作为web服务
const express = require('express') 

const app = express(); 
let browser; 
let page; 
(async () => { 
    const puppeteer = require('puppeteer'); 
    browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']}); 
    page = await browser.newPage(); 
})();

app.get('/word/:vocabulary', function (req, res) { 
    var url = req.params.url; 
    var vocabulary = req.params.vocabulary; 
    (async() => {
        await page.goto('http://www.iciba.com/'+vocabulary); 
        const html = await page.$eval('div.article div.article-section', e => e.outerHTML); 
        res.send(html);
    })();
}) 

app.listen(5000, function () {
    // do something
});
*/
