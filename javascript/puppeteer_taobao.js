const puppeteer =  require('puppeteer');
const chalk = require('chalk');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: '/Applications/Chromium.app/Contents/MacOS/Chromium',
        headless: true,
        slowMo: 200,
        ignoreHTTPSErrors: true,
        timeout: 30000
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

        await page.goto('https://s.taobao.com/search?q=gtx1080&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180416&ie=utf8');
        console.log(chalk.yellow('页面初次加载完毕'));

        const handleData = async() => {
            const list = await page.evaluate(() => {

                const writeDataList = [];

                let itemList = document.querySelectorAll('.item.J_MouserOnverReq');
                for (let item of itemList) {
                    let writeData = {};

                    let img = item.querySelector('img');
                    writeData.picture = img.src;

                    let link = item.querySelector('.pic-link.J_ClickStat.J_ItemPicA');
                    writeData.link = link.href;

                    let price = item.querySelector('strong');
                    writeData.price = ~~price.innerText;

                    let title = item.querySelector('.title>a');
                    writeData.title = title.innerText;

                    writeDataList.push(writeData);
                }
                return writeDataList;
            })
            // 写入数据库

            console.log(chalk.yellow('写入数据库完毕'));
        };

        for (let i = 1; i <= 50; i++) {
            const pageInput = await page.$(`.J_Input[type='number']`)
            const submit = await page.$('.J_Submit')
            await pageInput.type('' + i)
            await submit.click();
            await page.waitFor(2500);

            console.clear();
            console.log(chalk.yellow(formatProgress(i)));
            console.log(chalk.yellow('页面数据加载完毕'));

            await handleData();
            await page.waitFor(2500);
        }

        await browser.close();
        console.log(chalk.green('服务正常结束'));
    } catch (error) {
        console.log(error);
        console.log(chalk.red('服务意外终止'));
        await browser.close();
    } finally {
        console.log('xxx');
        process.exit(0);
    }
})();

function formatProgress(current) {
    let percent = (current / 50) * 100;
    let done = ~~(current / 50 * 40);
    let left = 40 - done;

    let str = `当前进度：[${''.padStart(done, '=')}${''.padStart(left, '-')}]   ${percent}%`;
    return str;
}
