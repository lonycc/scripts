'use strict';

var casper = require('casper').create({
    stepTimeout: 500000,
    verbose: true,
    logLevel: 'debug',
    pageSettings: {
        loadImages: true,
        loadPlugins: false,
        javascriptEnabled: true,
        userAgent: 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    },
    viewportSize: {
        width: 1280,
        height: 720
    },
    onError: function(self, m) {
        console.log('============onError===========:\n' + m);
        self.exit(1);
    }
});

casper.start('https://movie.douban.com/explore#!type=movie&tag=日本&sort=recommend&page_limit=20&page_start=0', function() {
    console.log('开始加载第一页');
});

var xLoadMoreBtn = {type: 'xpath', path: '//a[contains(text(), "加载更多")]'};

function addStep() {
    casper.waitForSelector(xLoadMoreBtn, function() {
        casper.capture('ok.png');
        casper.click(xLoadMoreBtn);
        addStep();
    }, function(){this.echo('未获取到数据');}, 10000);
}

addStep();

casper.run();
