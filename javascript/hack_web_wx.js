// ==UserScript==
// @name         网页微信伪装成云笔记
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       YGYOOO
// @match        https://wx2.qq.com/*
// @match        https://wx.qq.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    document.title = '云笔记';
// 监听title改变
new window.MutationObserver((mutations) => {
  mutations.forEach(() => {
    if (document.title !== '云笔记') document.title = '云笔记';
  });
}).observe(document.querySelector('head > title'), { subtree: true, characterData: true, childList: true })

// 按钮文字经常会被重置为”发送“，简单粗暴一点改回来
setInterval(() => {
  const btn = document.querySelector('.btn.btn_send');
  if (btn && btn.innerHTML !== '保存') btn.innerHTML = '保存';
}, 1000);

const style = document.createElement('style');
style.innerHTML=`
body {
  background: none !important;
}

.panel.give_me, .search_bar > input, .chat_item.active {
  background: none !important;
  color: #393939 !important;
}
#search_bar {
  padding: 8px 18px !important;
  width: 140px !important;
  margin: 0 !important;
}
#search_bar > input {
  border: 1px solid #e0e1e5;
  border-radius: 30px;
  width: 140px !important;
}

.chat_item .avatar img, .message img.avatar, .contact_item .avatar img, .header img  {
  opacity: 0 !important;
}

.chat_item {
  border-bottom: 1px solid #e0e1e5 !important;
}

.nav_view {
  top: 85px !important;
}

.download_entry {
  display: none !important;
}

.bubble.bubble_primary {
  background: none !important;
}
.bubble.bubble_primary::before, .bubble.bubble_primary::after {
  content: none !important;
}
.bubble.bubble_default {
  background: none !important;
}
.bubble.bubble_default::before, .bubble.bubble_default::after {
  content: none !important;
}

.nickname, .nickname_text, .chat_item.active .ext, .chat_item.active .info .msg {
  color: #393939 !important;
}
.recommendation .contact_item .nickname {
  color: white !important;
}
.tab {
  background: #e0e1e5 !important;
  padding-bottom: 0 !important;
}
.tab .tab_item:after {
  display: none !important;
}

.box {
  background: white !important;
}

.title_wrap {
  background: white !important;
}

.main {
  height: calc(100% - 50px) !important;
  display: flex !important;
  padding-top: 0 !important;
}

.main_inner {
  max-width: none !important;
  flex-grow: 10 !important;
}

.box_hd {
  text-align: left !important;
  border-bottom: 1px solid #e0e1e5;
}
.box_hd .title_wrap {
  border-bottom: none !important;
}

.header {
  padding: 0 !important;
  position: relative !important;
  height: 0 !important;
}
.header .opt {
  position: absolute !important;
  top: 10px;
  right: 20px;
}

.panel.give_me {
  width: 250px !important;
  border-right: 1px solid #e0e1e5;
}
.panel.give_me .tab:after {
  border-bottom: 1px solid #e0e1e5;
  left: 0 !important;
  right: 0 !important;
}

.contact_list .contact_title {
  background: none !important;
}
.contact_list .contact_item {
  border-bottom: 1px solid #e0e1e5 !important;
}
.contact_list .active {
  background: none !important;
}

.web_wechat_tab_chat_hl, .web_wechat_tab_public_hl, .web_wechat_tab_friends_hl {
  filter: blur(5px);
}



.weChatShelter-head {
  width: 100%;
  height: 50px;
  background: rgb(80, 139, 231);
}
.weChatShelter-head-left {
  height: 50px;
}
.weChatShelter-head-right {
  height: 50px;
  float: right;
}
.weChatShelter-menu {
  width: 80px;
  display: flex;
  flex-direction: column;
  background: rgb(245, 245, 245);
}
.weChatShelter-menu-top {
  width: 100%;
}
.weChatShelter-menu-bottom {
  width: 100%;
  margin-top: auto;
}
`;
document.documentElement.appendChild(style);
const style2 = document.createElement('style');
style2.innerHTML = `
.chat_item .avatar, .message .avatar, .contact_item .avatar {
  background-image: url(https://raw.githubusercontent.com/YGYOOO/WeChat-Shelter/master/project/images/note.jpg) !important;
  background-size: contain;
  background-repeat: no-repeat;
}
`;
document.documentElement.appendChild(style2);

var link = document.querySelector("link[rel*='icon']") || document.createElement('link');
link.type = 'image/x-icon';
link.rel = 'shortcut icon';
link.href = 'https://raw.githubusercontent.com/YGYOOO/WeChat-Shelter/master/project/images/note.jpg';
document.getElementsByTagName('head')[0].appendChild(link);

// const img = document.createElement('img');
// img.setAttribute('class', 'weChatShelter-head');
// img.setAttribute('src', chrome.extension.getURL('images/head.jpg'));
// document.body.insertBefore(img, document.body.firstChild);

const head = document.createElement('div');
head.setAttribute('class', 'weChatShelter-head');
head.innerHTML = `
<img class="weChatShelter-head-left" src="https://raw.githubusercontent.com/YGYOOO/WeChat-Shelter/master/project/images/head_left.png"></img>
<img class="weChatShelter-head-right" src="https://raw.githubusercontent.com/YGYOOO/WeChat-Shelter/master/project/images/head_right.png"></img>
`;
document.body.insertBefore(head, document.body.firstChild);


const menu = document.createElement('div');
menu.setAttribute('class', 'weChatShelter-menu');
menu.innerHTML = `
<img class="weChatShelter-menu-top" src="https://raw.githubusercontent.com/YGYOOO/WeChat-Shelter/master/project/images/menu_top.png"></img>
<img class="weChatShelter-menu-bottom" src="https://raw.githubusercontent.com/YGYOOO/WeChat-Shelter/master/project/images/menu_bottom.png"></img>
`;
document.querySelector('.main').insertBefore(menu, document.querySelector('.main_inner'));
})();
