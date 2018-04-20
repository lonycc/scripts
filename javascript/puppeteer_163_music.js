const puppeteer = require('puppeteer');
const chalk = require('chalk');
const fs = require('fs');

(async() => {
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

        await page.goto('https://music.163.com/#');
        // 点击搜索框 输入 鬼才会想起
        const musicName = '鬼才会想';
        await page.type('.txt.j-flag', musicName, { delay: 0 });

        // 回车
        await page.keyboard.press('Enter');

        // 获取歌曲列表的 iframe
        await page.waitFor(2000);
        let iframe = await page.frames().find(f => f.name() === 'contentFrame');
        const SONG_LS_SELECTOR = await iframe.$('.srchsongst');

        // 获取歌曲 鬼才会想起 的地址
        const selectedSongHref = await iframe.evaluate(e => {
            const songList = Array.from(e.childNodes);
            const idx = songList.findIndex(v => v.childNodes[1].innerText.replace(/\s/g, '') === '鬼才会想起');
            return songList[idx].childNodes[1].firstChild.firstChild.firstChild.href;
        }, SONG_LS_SELECTOR);

        // 进入歌曲页面
        await page.goto(selectedSongHref);

        // 获取歌曲页面嵌套的 iframe
        await page.waitFor(2000);
        iframe = await page.frames().find(f => f.name() === 'contentFrame');

        // 点击 展开按钮
        const unfoldButton = await iframe.$('#flag_ctrl');
        await unfoldButton.click();

        // 获取歌词
        const LYRIC_SELECTOR = await iframe.$('#lyric-content');
        const lyricCtn = await iframe.evaluate(e => {
            return e.innerText;
        }, LYRIC_SELECTOR);

        console.log(lyricCtn);

        // 截图
        await page.screenshot({
            path: '歌曲.png',
            fullPage: true,
        });

        // 写入文件
        let writerStream = fs.createWriteStream('lyric.txt');
        writerStream.write(lyricCtn, 'UTF8');
        writerStream.end();

        // 获取评论数量
        const commentCount = await iframe.$eval('.sub.s-fc3', e => e.innerText);
        console.log(commentCount);

        // 获取评论
        const commentList = await iframe.$$eval('.itm', elements => {
            const ctn = elements.map(v => {
                return v.innerText.replace(/\s/g, '');
            });
            return ctn;
        });
        console.log(commentList);

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
