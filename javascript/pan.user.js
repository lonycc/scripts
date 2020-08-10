// ==UserScript==
// @name         百度网盘播放倍速
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  百度网盘播放倍速
// @author       tony
// @match        https://pan.baidu.com/play/video*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    let videoSpeedElement = document.createElement("div"),
        currentHref = "",
        viewReportDiv;
    videoSpeedElement.setAttribute("id", "video_speed_div");

    let style = document.createElement("style");
    style.type = "text/css";
    style.innerHTML = "#video_speed_div button, #third_video_plugin_btn { outline: 0; padding: 3px 5px; margin-left: 10px; background-color: #e2e0e0; border: 0; color: #222; cursor: pointer;} .video_speed_div-button-active { border: 0!important; background-color: #ffafc9!important; color: #fff!important; }";
    document.getElementsByTagName("head").item(0).appendChild(style);

    let _interval = setInterval(function () {
        if (document.querySelector(".video-main") && document.getElementById("video_speed_div") === null) {
            addSpeedBtns();
        }
    }, 5000);

    function addSpeedBtns() {
        var videoTitleTag = document.querySelector(".video-title");
        videoTitleTag.style.marginBottom = "50px";

        initBtn();

        videoSpeedElement.style.width = "100%";
        videoSpeedElement.style.height = "24px";

        videoTitleTag.appendChild(videoSpeedElement);

        clearInterval(_interval);

        hightlightBtn("1");
    }

    function initBtn() {
        let speedArr = [0.5, 1, 1.5, 2, 2.5, 3, 4, 5];
        for (let i = 0; i < speedArr.length; i++) {
            let speed = speedArr[i];
            let btn = document.createElement("button");
            btn.innerHTML = "x" + speed;
            btn.style.width = "40px";
            btn.setAttribute("id", "third_video_plugin_btn_" + speed);
            btn.addEventListener("click", changeVideoSpeed);
            videoSpeedElement.appendChild(btn);
        }
    }

    function changeVideoSpeed(e) {
        let speed = parseFloat(e.target.innerHTML.replace("x", ""));
        hightlightBtn(speed);
        eval('videojs.getPlayers("video-player").html5player.tech_.setPlaybackRate(' + speed + ');');
    }

    function hightlightBtn(speed) {
        let currentSpeedBtn = document.getElementById("third_video_plugin_btn_" + speed);
        if (currentSpeedBtn && currentSpeedBtn.className.indexOf("video_speed_div-button-active") === -1) {
            for (let i = 0; i < videoSpeedElement.childNodes.length; i++) {
                let btn = videoSpeedElement.childNodes[i];
                btn.setAttribute("class", "");
            }
            currentSpeedBtn.setAttribute("class", "video_speed_div-button-active");
        }
    }
})();
