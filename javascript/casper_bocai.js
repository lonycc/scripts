'use strict';

var system = require('system');
var os = system.os;
if ( os.name === 'windows' )
{
    phantom.outputEncoding = 'GBK';
}

var begin_time = Date.parse(new Date());
var casper = require('casper').create({
    stepTimeout: 500000,
    //clientScripts: [],
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

var username = casper.cli.has('username') ? casper.cli.get('username') : 'lidahai';
var password = casper.cli.has('password') ? casper.cli.get('password') : 'aaaa0000';
var type = casper.cli.has('type') ? casper.cli.get('type') : '';
var verify = casper.cli.has('verify') ? casper.cli.get('verify') : '';
var money = casper.cli.has('money') ? casper.cli.get('money') : '10';
var verify_code = '1234';

casper.start('https://w7300.com/top.php', function() {
    if ( verify !== 'outer' )
    {
        verify_code = this.evaluate(function() {
            var image = document.querySelector('#checkNum_img');
            var canvas = document.createElement('canvas');
            var ctx = canvas.getContext('2d');
            var numbers = [
                '0000110000011110001100110110000101100001011000010110000100110011000111100000110000000000000000000000000000000000000000000000000000000000',
                '0000110000011100001111000000110000001100000011000000110000001100000011000011111100000000000000000000000000000000000000000000000000000000',
                '0001111000110011011000010000000100000011000001100000110000011000001100000111111100000000000000000000000000000000000000000000000000000000',
                '0011111001100011000000010000001100001110000000110000000100000001011000110011111000000000000000000000000000000000000000000000000000000000',
                '0000001100000111000011110001101100110011011000110111111100000011000000110000001100000000000000000000000000000000000000000000000000000000',
                '0111111101100000011000000110111001110011000000010000000101100001001100110001111000000000000000000000000000000000000000000000000000000000',
                '0001111000110011011000010110000001101110011100110110000101100001001100110001111000000000000000000000000000000000000000000000000000000000',
                '0111111100000001000000010000001100000110000011000001100000110000011000000110000000000000000000000000000000000000000000000000000000000000',
                '0001111000110011011000010011001100011110001100110110000101100001001100110001111000000000000000000000000000000000000000000000000000000000',
                '0001111000110011011000010110000100110011000111010000000100100001001100110001111000000000000000000000000000000000000000000000000000000000'
            ];
            var captcha = '';
            canvas.width = 50;
            canvas.height = 20;
            document.body.appendChild(canvas);
            ctx.drawImage(image, 0, 0);
            for (var i = 0; i < 4; i++) {
                var pixels = ctx.getImageData(9 * i + 6, 6, 8, 17).data;
                var ldString = '';
                for (var j = 0; j < pixels.length; j += 4) {
                    ldString = ldString + (+(pixels[j] * 0.3 + pixels[j + 1] * 0.59 + pixels[j + 2] * 0.11 >= 140));
                }
                var comms = numbers.map(function(value) {
                    return ldString.split('').filter(function(v, index) {
                        return value[index] === v;
                    }).length;
                });
                captcha += comms.indexOf(Math.max.apply(null, comms));
            }
            return captcha;
        });
    } else {
        console.log('开启子线程识别验证码');
    }
});

if ( verify === 'outer' )
{
    casper.then(function() {
        this.captureSelector('verify.png', '#checkNum_img');
    });

    var spawn = require('child_process').spawn;
    casper.then(function() {
        var child = spawn('python3', ['verify_code.py']);
        child.stdout.on('data', function(data) {
            verify_code = data.split('\n')[0];
            console.log('当前验证码为 :' + verify_code);
        });
        child.stderr.on('data', function(data) {
            console.log('子进程执行出错: '+data.toString());
        });
        child.on('close', function(code) {
            console.log('子进程退出码: ' + code);
        });
    });
}

casper.wait(1000, function() {
    this.evaluate(function(username, password, verify_code) {
        document.getElementById('username').value = username;
        document.getElementById('password').value = password;
        document.getElementById('vlcodes').value = verify_code;
        document.getElementsByName('formsub')[0].click();
    }, username, password, verify_code);
    this.wait(3000, function() {
        if ( ! this.exists('#tz_money') )
        {
            this.echo('登录失败, 请检查账号密码是否正常');
            casper.exit(1);
        }
    });
});

if ( type === 'info' )
{
    casper.then(function() {
        var tz_money = this.evaluate(function() {
            return document.querySelector('#tz_money').innerText;
        });
        var user_money = this.evaluate(function() {
            return document.querySelector('#user_money').innerText;
        });
        this.echo(JSON.stringify({'username': username, 'tz_money': tz_money, 'user_money': user_money}));
    });
} else if ( type === 'history' ) {
    casper.then(function() {
        this.clickLabel('账户历史', 'a');
    });
    casper.withFrame('mainFrame', function() {
        this.click('input.subcla1');
        this.wait(2000, function() {
            var data = this.evaluate(function() {
                var table = document.querySelector('table.waikuang');
                var td = table.querySelectorAll('tr td');
                var arr = [];
                for (var i=0;i<td.length;i++)
                {
                    arr.push(td[i].innerHTML);
                }
                return arr;
            });
            this.echo(data);
        });
    });
} else if ( type === 'danshi' || type === 'gunqiu' ) {
    casper.then(function() {
        var url = 'https://w7300.com/show/ft_'+type+'_data.php?leaguename=&CurrPage=0&callback=ft_'+type+'_data&_='+Date.parse(new Date());
        this.open(url, {
            method: 'get',
            encoding: 'utf-8',
            headers: {
                'Referer': 'https://w7300.com/show/ftz_'+type+'.html',
                'X-Requested-With': 'XMLHttpRequest'
            }
        });
    });
    casper.then(function() {
        var arr = [];
        var data = this.getPageContent();
        var data_json = JSON.parse(trimJsonp(data));
        arr.push(data_json);
        var times = data_json.fy.p_page - 1;
        var i = 1;
        this.repeat(times, function() {
            var url = 'https://w7300.com/show/ft_'+type+'_data.php?leaguename=&CurrPage='+i+'&callback=ft_'+type+'_data&_='+Date.parse(new Date());
            this.open(url, {
                method: 'get',
                encoding: 'utf-8',
                headers: {
                    'Referer': 'https://w7300.com/show/ftz_'+type+'.html',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            this.then(function() {
                var data = this.getPageContent();
                var data_json = JSON.parse(trimJsonp(data));
                arr.push(data_json);
            });
            i++;
        });
        this.wait(times * 1000, function() {
            this.echo(JSON.stringify(arr));
        });
    });
} else if ( type === 'tz' ) {
    casper.thenOpen('https://w7300.com/', function() {
        this.click('.buttonDivInput');
    });

    casper.withFrame('leftFrame', function() {
        this.evaluate(function() {
            document.querySelector('#Label0').style.display = "block";
        });
        this.click('ul#Label0');
        this.click('ul#Label0 li:nth-child(1) a');
    });

    casper.withFrame('mainFrame', function() {
        this.waitForSelector('.bisai', function() {
            var atag = {type: 'xpath', path: '//a[contains(@onclick, "javascript:setbet(\'足球单式\',\'让球-客让1.5-斯摩棱斯克\',\'2937608\',\'Match_Ho\',\'1\',\'0\',\'斯摩棱斯克\');")]'};
            if ( this.exists(atag) )
            {
                this.click(atag);
                this.wait(1000, function() {
                    this.switchToMainFrame();
                    this.withFrame('leftFrame', function() {
                        this.thenEvaluate(function(money) {
                            document.getElementById('bet_money').value = money;
                            document.getElementById('submit_from').click();
                        }, money);
                        this.waitForAlert(function(response) {
                            this.echo(response.data);
                        });
                        this.capture('demo.png');
                    });
                });
            } else {
                this.echo('赛事不存在');
            }
        }, function(){this.echo('未获取到比赛数据');}, 10000);
    });

} else {
    casper.then(function() {
        this.exit(1);
    });
}

function trimJsonp(data)
{
    var begin = data.indexOf('(');
    var end = data.lastIndexOf(')');
    if ( begin > -1 && end > begin )
    {
        return data.substring(begin+1, end);
    }
    return data;
}

casper.run(function() {
    var end_time = Date.parse(new Date());
    this.echo('耗时: ' + ((end_time - begin_time) / 1000) + '秒');
    this.exit(1);
});
