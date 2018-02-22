// ==UserScript==
// @name           Douban Download Search（支持https）
// @namespace      https://github.com/ywzhaiqi
// @description    增加豆瓣电影、图书，音乐的下载搜索链接
// @author         peter(原作者ywzhaiqi） 维护者liubinyan @豆瓣
// @version        1.5.7
// @include        *//movie.douban.com/subject/*
// @include        *//music.douban.com/subject/*
// @include        *//book.douban.com/subject/*
// @grunt          none
// ==/UserScript==

function run () {
	var movieTitle = $('h1 span:eq(0)').text();
	var title = $('html head title').text();
	var keyword1 = title.replace( '(豆瓣)', '' ).trim();
	var keyword2 = encodeURIComponent( keyword1 );
	var keyword3 = encodeURIComponent( keyword2 );
	var MovieOriginalTitle = movieTitle.replace(/^[^a-zA-Z]*/, "");
	var movieSimpleTitle = keyword1.replace(/第\S+季.*/, "");
	var movieFinalTitle = MovieOriginalTitle.replace(/Season\s/, "S");

	var Movie_links = [
		// { html: "百度盘", href: "http://www.baidu.com/s?wd=" + encodeURIComponent(keyword1 + " site:pan.baidu.com")},
		{ html: "磁力数据库", href: "http://cilidb.net/page/"+keyword1+"/1-0-0.shtml"},
		{ html: "磁力吧", href: "https://www.ciliba.org/s/"+keyword1+".html"},
		{ html: "btdigg", href: "http://btdiggs.com/search/"+keyword2+"/1/0/0.html"},
		{ html: "torrentkitty", href: "https://tw.torrentkitty.tv/search/"+keyword1+"/"},
		{ html: "西林街", href: "http://www.xilinjie.com/s?q="+keyword1},
		{ html: "胖次", href: "http://www.panc.cc/s/"+keyword1+"/td_0"},
		{ html: "盘搜", href: "http://pansou123.com/?search="+keyword1},
		{ html: "百度盘", href: "http://pansou.com/?q=" + keyword1},
		{ html: "zimuzu", href: "http://www.zimuzu.tv/search/index?keyword=" + movieSimpleTitle },
		{ html: "天天美剧", href: "http://www.ttmeiju.vip/index.php/search/index.html?keyword=" + movieSimpleTitle },
		{ html: "Torrentseeker", href: "https://torrentseeker.com/search.php?q=" + keyword2 },
		{ html: "逛电驴", href: "http://verycd.gdajie.com/find.htm?keyword=" + keyword2 },
		{ html: "ACG狗狗", href: "http://bt.acg.gg/search.php?keyword=" + keyword2 },
		{ html: "电影首发站", href: "http://www.dysfz.cc/key/" + keyword1 +"/" },
		{ html: "KickAss", href: "https://kickass2.ch/usearch/" + movieFinalTitle +"/" },
		{ html: "胖鸟电影", href: "http://www.pniao.com/Mov/so/" + keyword1},
		{ html: "憨憨电影", href: "https://www.hanhanfilm.com/search/keyword?q=" + keyword1},
		{ html: "ED2000", href: "http://www.ed2000.me/search.aspx?SearchWord=" + keyword1 + "&searchMethod=ED2000"},
		{ html: "The Pirate Bay", href: "https://thepiratebay.org/search/" + movieFinalTitle},
		{ html: "RARBG", href: "https://rarbg.is/torrents.php?search=" + movieFinalTitle + "&category[]=14&category[]=48&category[]=17&category[]=44&category[]=45&category[]=47&category[]=50&category[]=51&category[]=52&category[]=42&category[]=46&category[]=18&category[]=41&category[]=49"},
		{ html: "磁力猫", href: "http://www.cilimao.me/search?word=" + keyword1 + "&page=1"},
		{ html: "BT之家", href: "http://www.btbtt88.com/search-index-keyword-" + keyword1 + ".htm" },
		{ html: "BT蚂蚁", href: "http://www.btmyi.com/search.html?kw=" + keyword1},
		{ html: "MiniMP4", href: "http://www.minimp4.com/search?q=" + keyword1},
	];
	var Music_links = [
		{ html: "百度盘", href: "http://pansou.com/?q=" + keyword1},
		{ html: "BOXSET.RU", href: "http://boxset.ru/?s=" + keyword1},
		{ html: "KickAss", href: "https://kickass2.ch/usearch/" + keyword1 +"/" },
		{ html: "逛电驴", href: "http://verycd.gdajie.com/find.htm?keyword=" + keyword2 },
		{ html: "爱无损", href: "http://www.lovewusun.com/?s=" + keyword1},
		{ html: "漫音社", href: "http://www.acgjc.com/?s=" + keyword1},
		{ html: "TPARSER", href: "http://tparser.org/" + keyword1},
		{ html: "无损迷", href: "http://zhannei.baidu.com/cse/search?s=7434802276389067349&entry=1&q=" + keyword1},
		{ html: "Lossless Music Archives", href: "http://losslessma.net/?s=" + keyword1 + "&searchsubmit=U"},
	];
	var Book_links = [
		{ html: "百度盘", href: "http://pansou.com/?q=" + keyword1},
		{ html: "微盘", href: "https://duckduckgo.com/?q=" + keyword1 + " site%3Avdisk.weibo.com&ia=web"},
		{ html: "mLook", href: "http://www.mlook.mobi/search?q=" + keyword2 },
		{ html: "Library Genesis", href: "http://libgen.io/search.php?req=" + keyword1 + "&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"},
		{ html: "ebook3000", href: "http://ebook3000.com/plus/search.php?keyword=" + keyword1 + "&x=0&y=0"},
		{ html: "Torrentseeker", href: "https://torrentseeker.com/search.php?q=" + keyword2 },
		{ html: "新浪爱问", href: "http://ishare.iask.sina.com.cn/search/0-0-all-1-default?cond=" + keyword3 },
		{ html: "Readfree",href: "http://readfree.me/search/?q=" + keyword1 },
		{ html: "周读",href: "http://ireadweek.com/index.php/Index/bookList.html?keyword=" + keyword1 },
		{ html: "我的小书屋",href: "http://mebook.cc/?s=" + keyword1 },
		{ html: "逛电驴", href: "http://verycd.gdajie.com/find.htm?keyword=" + keyword2 },
		{ html: "读秀@RUC", href: "https://vpn.ruc.edu.cn/,DanaInfo=book.duxiu.com+search?Field=all&channel=search&sw=" + keyword1 + "&ecode=utf-8&edtype=&searchtype=&view=0"},
		{ html: "云海电子图书馆",href: "http://www.pdfbook.cn/?s=" + keyword1 },
		{ html: "书语者",href: "https://book.shuyuzhe.com/search/" + keyword1 },
		{ html: "Mobilism", href: "https://forum.mobilism.org/search.php?keywords=" + keyword1 + "&fid[]=0&sc=1&sr=topics&sf=titleonly"},
		{ html: "超星", href: "http://book.chaoxing.com/search/all/" + keyword1 + "/bookList1_.html"},
		{ html: "So-Kindle",href: "https://www.so-kindle.com/q?type=1&keyword=" + keyword1 },
		{ html: "SoKindle", href: "https://sokindle.com/search/" + keyword2 },
		{ html: "国学大师", href: "http://www.guoxuedashi.com/so.php?sokeytm=" + keyword1 + "&ka=100&submit="},
		{ html: "中國哲學書電子化計劃", href: "http://ctext.org/searchbooks.pl?if=gb&searchu=" + keyword1 },
		{ html: "Kindleshare", href: "http://sk.kindleshare.cn/?q=" + keyword1 + "&submit=Search"},
		{ html: "WorldCat",href: "https://www.worldcat.org/search?qt=worldcat_org_all&q=" + keyword1 },
	];
	var Str_links = [
		{ html: "伪·射手网", href: "https://secure.assrt.net/sub/?searchword=" + keyword1},
		{ html: "Subscene", href: "https://subscene.com/subtitles/title?q=" + movieFinalTitle + "&l="},
		{ html: "日语字幕网", href: "http://jpsubtitle.com/?s=" + keyword1},
	];
	var Buy_links = [
		{ html: "淘宝", href: "https://s.taobao.com/search?q=" + keyword1},
		{ html: "Amazon", href: "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + keyword1},
		{ html: "澜瑞外文", href: "https://www.lanree.com/search?keywords=" + keyword1},
		{ html: "蔚蓝网", href: "http://www.wl.cn/search?keywords=" + keyword1},
		{ html: "Book Depository", href: "https://www.bookdepository.com/search?searchTerm=" + keyword1 + "&search=Find+book"},
		{ html: "アマゾン", href: "https://www.amazon.co.jp/s/ref=nb_sb_noss?__mk_ja_JP=カタカナ&url=search-alias%3Daps&field-keywords=" + keyword1},
		{ html: "多抓鱼", href: "http://www.duozhuayu.net/search/" + keyword1},
		{ html: "博客來", href: "http://search.books.com.tw/search/query/key/" + keyword1 + "/cat/all"},
		{ html: "AbeBooks", href: "https://www.abebooks.com/servlet/SearchResults?sts=t&tn=" + keyword1},
		{ html: "Buchmarie", href: "https://www.buchmarie.de/Startseite.aspx?q=" + keyword1},
		{ html: "缺书网", href: "http://www.queshu.com/search/?c=" + keyword1},
		{ html: "三民書店", href: "http://www.sanmin.com.tw/search/index/?ct=K&qu=" + keyword1 + "&ls=SD"},
	];

	var link = $("<div>").append(
		$("<span>").attr("class", "pl").html("传送链接:")
	);
	switch(location.host){
		case "movie.douban.com":
			appendLinks(Movie_links, link);
			link.append('<br>').append('<span class="pl">字幕链接:</span>');
			appendLinks(Str_links, link);
			break;
		case "book.douban.com":
			appendLinks(Book_links, link);
            link.append('<br>').append('<span class="pl">购买链接:</span>');
			appendLinks(Buy_links, link);
			break;
		case "music.douban.com":
			appendLinks(Music_links, link);
			break;
	}

	$('#info').append(link);

	function appendLinks(items, appendTo){
		items.forEach(function(item, i){
			$("<a>")
				.html(item.html)
				.attr({
					href: item.href,
					target: "_blank"
				})
				.appendTo(appendTo);

			if(i != items.length -1){
				appendTo.append(" / ");
			}
		});
	}
}

run();
