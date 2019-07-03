const puppeteer =  require('puppeteer-core');
const chalk = require('chalk');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: '/Applications/Chromium.app/Contents/MacOS/Chromium',
        headless: true,
        slowMo: 200,
        ignoreHTTPSErrors: true,
        timeout: 40000,
    });
    console.log(chalk.green('服务正常启动'));

    try {
        const page = await browser.newPage();
        await page.setRequestInterception(true);

        page.on('request', request => {
            if (request.resourceType() === 'image')
                request.abort();
            else
                request.continue();
        });
        page.on('console', msg => {
            if (typeof msg === 'object') {
                console.dir(msg);
            } else {
                console.log(chalk.blue(msg));
            }
        });

        await page.goto('http://m.toutiao.com/profile/50502347096/#mid=50502347096', {
            timeout: 30000,
            waitUntil: 'domcontentloaded',
        });

        const articleNav = '#navlist>a[data-type=all]';

        await page.click(articleNav);
        const article_list = '.list-content.feed.all';

        await page.waitForSelector(article_list);

        // 滚屏
        await page.evaluate(() => {
            for (var y = 0; y <= 20000; y += 100) {
                window.scrollTo(0, y);
            }
        });
        await page.waitFor(5000);

        const tcs = await page.evaluate((selector) => {
            const articles = Array.from(document.querySelector(selector).querySelectorAll('section'));
            return articles.map(article => {
                const title = article.querySelector('h3').textContent;
                const read = article.querySelector('.label-count').textContent.trim();
                const comment = article.querySelector('.label-comment').textContent;
                const src = article.querySelector('.label-src').textContent;
                const time = article.querySelector('.time').getAttribute('title');
                const url = article.querySelector('a').getAttribute('href');
                return `${title} [${url}] [${time}] [${src}] [${read}] [${comment}]\n`;
            });
        }, article_list);

        console.log(tcs.join('\n'));
        console.log(tcs.length);
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
