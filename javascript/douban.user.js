// ==UserScript==
// @name           豆瓣增强工具
// @namespace      https://github.com/lonycc
// @description    增加豆瓣电影、图书，音乐的下载搜索链接
// @author         peter
// @version        0.0.1
// @include        http*://movie.douban.com/subject/*
// @include        http*://music.douban.com/subject/*
// @include        http*://book.douban.com/subject/*
// @grunt          none
// ==/UserScript==

(function() {
    'use strict';

    let movieTitle = document.querySelector('h1>span:first-child').innerText;
    let title = document.querySelector('head>title').innerText;
    let keyword1 = title.replace('(豆瓣)', '').trim();
    let keyword2 = encodeURIComponent(keyword1);
    let keyword3 = encodeURIComponent(keyword2);
    let MovieOriginalTitle = movieTitle.replace(/^[^a-zA-Z]*/, "");
    let movieSimpleTitle = keyword1.replace(/第\S+季.*/, "");
    let movieFinalTitle = MovieOriginalTitle.replace(/Season\s/, "S");

    let Movie_links = [
        { html: "zxf", href: "http://zhuixinfan.com/main.php" },
        { html: "ku", href: `http://kukutu.tv/search.php`},
        { html: "slimego", href: `http://www.slimego.cn/search.html?q=${keyword1}` },
        { html: "rrys", href: `http://www.zmz2020.com/search/index?keyword=${movieSimpleTitle}` },
        { html: "hpjav", href: "https://hpjav.tv/" },
        { html: "sep", href: "http://sezhanxx.net/" },
        { html: "spankbang", href: "https://spankbang.com/" },
        { html: "carib", href: "https://www.caribbeancom.com/actress/a.html" },
        { html: "vip", href: "http://www.guandianzhiku.com/v/s" },
    ];
    let Music_links = [
        { html: "vip", href: `http://mctool.cn/music/?page=audioPage&type=migu&name=${keyword1}` },
        { html: "盘搜", href: `http://pansou.com/?q=${keyword1}` },
        { html: "爱无损", href: `http://www.lovewusun.com/?s=${keyword1}` },
        { html: "漫音社", href: `http://www.acgjc.com/?s=${keyword1}` },
    ];
    let Book_links = [
        { html: "磁力", href: `https://www.wocali.com/s/search.action?q=${keyword1}&currentPage=1` },
        { html: "微盘", href: `https://duckduckgo.com/?q=${keyword1} site%3Avdisk.weibo.com&ia=web` },
        { html: "iask", href: `http://ishare.iask.sina.com.cn/search/0-0-all-1-default?cond=${keyword3}` },
        { html: "pdf", href: `http://www.pdfbook.cn/?s=${keyword1}` },
        { html: "超星", href: `http://book.chaoxing.com/search/all/${keyword1}/bookList1_.html` },
        { html: "国学", href: `http://www.guoxuedashi.com/so.php?sokeytm=${keyword1}&ka=100&submit=` },
        { html: "WC", href: `https://www.worldcat.org/search?qt=worldcat_org_all&q=${keyword1}` },
    ];
    let Str_links = [
        { html: "伪·射手网", href: `http://assrt.net/sub/?searchword=${keyword1}` },
        { html: "字幕库", href: `http://www.zimuku.la/search?q=${keyword1}` },
    ];
    let Buy_links = [
        { html: "当当网", href: `http://search.dangdang.com/?key=${keyword2}&category_path=01.00.00.00.00.00#J_tab` },
        { html: "Amazon", href: `https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=${keyword1}` },
        { html: "澜瑞外文", href: `https://www.lanree.com/search?keywords=${keyword1}` },
        { html: "蔚蓝网", href: `https://www.wl.cn/search?keywords=${keyword1}` },
        { html: "多抓鱼", href: `https://www.duozhuayu.com/search/${keyword1}` },
        { html: "博客來", href: `http://search.books.com.tw/search/query/key/${keyword1}/cat/all` },
        { html: "缺书网", href: `http://www.queshu.com/search/?c=${keyword1}` },
        { html: "三民書店", href: `http://www.sanmin.com.tw/search/index/?ct=K&qu=${keyword1}&ls=SD` },
    ];

    function appendTags() {
        let link = document.createElement("div");
        let span = document.createElement("span");
        span.setAttribute("class", "pl");
        span.innerText = "传送链接: ";
        link.appendChild(span);
        let br = document.createElement("br");
        let zimu = document.createElement("span");
        zimu.setAttribute("class", "pl");
        zimu.innerText = "字幕链接: ";
        let buy = document.createElement("span");
        buy.setAttribute("class", "pl");
        buy.innerText = "购买链接: ";

        switch (window.location.host) {
            case "movie.douban.com":
                appendLinks(Movie_links, link);
                link.appendChild(br);
                link.appendChild(zimu);
                appendLinks(Str_links, link);
                break;
            case "book.douban.com":
                appendLinks(Book_links, link);
                link.appendChild(br);
                link.appendChild(buy);
                appendLinks(Buy_links, link);
                break;
            case "music.douban.com":
                appendLinks(Music_links, link);
                break;
        }

        document.querySelector('#info').appendChild(link);
    }

    function appendLinks(items, parent) {
        items.forEach(function(item, i) {
            let a = document.createElement("a");
            a.setAttribute("href", item.href);
            a.setAttribute("target", "_blank");
            a.innerText = item.html;
            a.style.marginLeft = '5px';
            parent.appendChild(a);
        });
    }

    appendTags();
})();
