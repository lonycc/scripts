const puppeteer = require('puppeteer');
const chalk = require('chalk');

(async() => {
    const browser = await puppeteer.launch({
        executablePath: '/Applications/Chromium.app/Contents/MacOS/Chromium',
        headless: true,
        slowMo: 200,
        ignoreHTTPSErrors: true,
        timeout: 10000
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
        await page.goto('https://jandan.net/duan/page-94#comments');
        const commentBtn = '.tucao-btn';
        await page.click(commentBtn);

        const tucao = '.jandan-tucao';
        const tucao_hot = '.tucao-hot';
        const tucao_list = '.tucao-list';
        const tucao_more = 'div.jandan-tucao-more:not([style])';
        await page.waitForSelector(tucao);

        const cmts = await page.evaluate( (selector, more) => {
            const tucaos = Array.from(document.querySelector(selector).querySelectorAll('.tucao-row'));
            return tucaos.map(comment => {
                const author = comment.querySelector('.tucao-author').textContent;
                const content = comment.querySelector('.tucao-content').textContent.trim();
                const oo = comment.querySelector('.tucao-oo').textContent;
                const xx = comment.querySelector('.tucao-xx').textContent;
                return `${author} oo[${oo}] xx[${xx}]: \n${content}\n`;
            });
        }, tucao_list, tucao_more);

        console.log(cmts.join('\n'));

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
