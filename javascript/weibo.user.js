// ==UserScript==
// @name         追踪微博图床上传者
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  快速找到微博图床图片的上传者。
// @author       You
// @match        *://*.sinaimg.cn/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    function string62to10(number_code) {
        number_code = String(number_code);
        var chars = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ',
            radix = chars.length,
            len = number_code.length,
            i = 0,
            origin_number = 0;
        while (i < len) {
            origin_number += Math.pow(radix, i++) * chars.indexOf(number_code.charAt(len - i) || 0);
        }
        return origin_number;
    }
    function decode(url) {
        var lastIndexOfSlash = url.lastIndexOf('/');
        var number = url.substr(lastIndexOfSlash + 1, 8);
        if (number.startsWith('00')) {
            return string62to10(number);
        } else {
            return parseInt(number, 16);
        }
    }
    window.location = 'https://weibo.com/u/' + decode(window.location.href);
})();
