const puppeteer = require('puppeteer');
const chalk = require('chalk');

(async() => {
    const browser = await puppeteer.launch({
        executablePath: '/Applications/Chromium.app/Contents/MacOS/Chromium',
        headless: true,
        slowMo: 200,
        ignoreHTTPSErrors: true,
        timeout: 10000,
    });
    console.log(chalk.green('服务正常启动'));
    try {
        const page = await browser.newPage();

        page.on('console', msg => {
            if (typeof msg === 'object') {
                console.dir(msg);
            } else {
                console.log(chalk.blue(msg));
            }
        });

        // 进入页面
        await page.goto('https://jandan.net/duan', {
            timeout: 10000,
            waitUntil: 'domcontentloaded',
        });

        // 解析当前页列表
        /*
        await page.evaluate(() => {
            const cmmts = Array.from(document.querySelectorAll('.row'));
            return cmmts.map(cmmt => {
                const author = cmmt.querySelector('.author>strong').textContent;
                const content = cmmt.querySelector('.text').textContent;
                const oo = cmmt.querySelector('.tucao-like-container').textContent;
                const xx = cmmt.querySelector('.tucao-unlike-container').textContent;
                const tucao = cmmt.querySelector('.tucao-btn').textContent;
                console.log(`${author} ${oo} ${xx} ${content}`.trim('\n'));
            });
        });
        */

        const tucaoBtn = '.tucao-btn';

        // 点击所有的吐槽按钮
        /*
        await page.evaluate(commentBtn => {
            let btns = document.querySelectorAll(tucaoBtn);
            btns.forEach(el => el.click());
        }, commentBtn);
        */

        // 点击第一个吐槽按钮
        await page.click(tucaoBtn);

        const tucao = '.jandan-tucao';
        const tucao_hot = '.tucao-hot';
        const tucao_list = '.tucao-list';
        const tucao_more = 'div.jandan-tucao-more:not([style])';
        await page.waitForSelector(tucao);

        const tcs = await page.evaluate((selector, more) => {
            const tucaos = Array.from(document.querySelector(selector).querySelectorAll('.tucao-row'));
            return tucaos.map(tucao => {
                const author = tucao.querySelector('.tucao-author').textContent;
                const content = tucao.querySelector('.tucao-content').textContent.trim();
                const oo = tucao.querySelector('.tucao-oo').textContent;
                const xx = tucao.querySelector('.tucao-xx').textContent;
                return `${author} oo[${oo}] xx[${xx}]: \n${content}\n`;
            });
        }, tucao_list, tucao_more);

        console.log(tcs.join('\n'));

        await browser.close();
        console.log(chalk.green('服务正常结束'));
    } catch (error) {
        console.log(error);
        console.log(chalk.red('服务意外终止'));
        await browser.close();
    } finally {
        process.exit(0);
    }
})();
