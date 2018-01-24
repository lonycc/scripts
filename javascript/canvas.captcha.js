// ==UserScript==
// @name         利用cavas识别验证码
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description 验证码识别
// @author       tony
// @match        http://www.domain.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    /*
    var image = document.querySelector('img');                 //获取到验证码图片
    var canvas = document.createElement('canvas');                        //新建一个canvas
    var ctx = canvas.getContext('2d');                                    //获取2D上下文
    var numbers = [];                                                     //存储数字模板的数组
    canvas.width = Object.prototype.hasOwnProperty.call(image, 'width') ? image.width : 50;                                           //设置canvas的宽度
    canvas.height = Object.prototype.hasOwnProperty.call(image, 'width') ? image.height : 20;                                         //设置canvas的高度
    document.body.appendChild(canvas);                                    //将canvas添加进document
    ctx.drawImage(image, 0, 0);                                           //将验证码绘制到canvas上
    for (var i = 0; i < 4; i++) {                                         //循环四次,识别四个数字
        var pixels = ctx.getImageData(9 * i + 6, 6, 8, 17).data;         //按照公式获取到每个数字上的像素点, 用ps打开图片分析像素坐标
        var ldString = '';                                                //用来存储明暗值的字符串
        for (var j = 0, length = pixels.length; j < length; j += 4) {                 //每次循环取四个值,分别是一个像素点的r,g,b,a值
            ldString = ldString + (+(pixels[j] * 0.3 + pixels[j + 1] * 0.59 + pixels[j + 2] * 0.11 >= 128));     //灰度化+二值化,但我们并没有真正的处理图像
        }
        console.log(ldString);                 //输出存储着明暗值的字符串
    }
    */
    
    var image = document.querySelector('img');
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    var numbers = [ //模板,依次是0-9十个数字对应的明暗值字符串
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
    console.log('the verify code is: ' + captcha);
})();
