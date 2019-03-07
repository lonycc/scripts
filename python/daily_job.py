#!/usr/bin/env python3
# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

s = requests.Session()
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
'Connection': 'keep-alive',
'Host': '',
'Referer': '',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.3 Safari/537.36'    
}

def guanren(start=42219, end=42250):
    fs = open('p.md', 'a+')
    for i in range(start, end):
        url = 'https://www.guanren4.com/play/{}.html'.format(i)
        print(i)
        r = s.get(url, timeout=30)
        soup = BS(r.text, 'html.parser')
        title = soup.find('div', class_='block_title')
        if title:
            title = title.text
            title = title.strip('[').replace(']', ' ')
            video_url = 'https://www.didiaass.com/filets/{0}/list.m3u8'.format(i)
            fs.write('[' + title + '](' + video_url +')\n\n')
    fs.close()
    print('finished')

def jporn():
    for i in range(3011, 3050):
        url = 'http://jporn.link/units/{0}'.format(i)
        rs = s.get(url, headers=headers, timeout=10)
        soup = bs(rs.text, "html.parser")
        video = soup.find('source')
        if video:
            p = urljoin(url, video.get('src'))
            print(f'[]({p})')
    print('finished')

def fuliba(start_url = 'http://fulibus.net/page/1'):
    rs =  s.get(start_url, headers=headers, timeout=10)
    if rs.status_code == 200:
        soup = bs(rs.text, 'html.parser')
        h2 = soup.find_all('h2', class_="entry-name")
        if h2:
            titles = [h.find('a').text.strip('\n').strip() for h in h2]
            detail_url = [h.find('a').get('href') for h in h2]
            for i in range(0, len(titles)):
                print('<p><a target="__blank" href="{0}">{1}</a></p>'.format(detail_url[i], titles[i]))

def tumblr(start=400, end=1500):
    for i in range(1558, 1583):
        url = 'http://mar-bee.tumblr.com/page/{0}'.format(i)
        #print(f'now page {i}')
        r = s.get(url, timeout=6)
        soup = bs(r.text, 'html.parser')
        posts = soup.find_all('div', class_='post-photo')
        #posts = soup.find_all('img', class_='photo')
        for post in posts:
            print(post.find('img').get('src'))
            #print(post.get('src'))
        time.sleep(0.1)
    print('finish')

def t66y(url):
    r = s.get(url, timeout=6, proxies={'http': 'http://127.0.0.1:1087'})
    soup = bs(r.text, 'html.parser')
    content = soup.find('div', class_='tpc_content do_not_catch')
    for img in content.find_all('img'):
        print(img.get('src'))

def maimai():
    url = 'https://acc.maimai.cn/reg0?fr=&uidtype=0&regfr=&abtype=&udef_data=-1&cusdata=&ab=a'
    r = s.post(url, 
               timeout=10, 
               data={'fr': '', 'payload': '', 'uidtype': 0, 'u': 0, 'tel': 15011971011},
               headers={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
                'cache-control': 'max-age=0',
                'referer': 'https://acc.maimai.cn/reg0?fr=&uidtype=0&regfr=&abtype=&udef_data=-1&cusdata=&ab=a',
                'upgrade-insecure-requests': '1',
                'origin': 'https://acc.maimai.cn',
                'content-type': 'application/x-www-form-urlencoded',
                'content-length': '42',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.3 Safari/537.36' 
               }
              )
    soup = bs(r.text, 'html.parser')
    ul = soup.find('ul', class_='regList')
    if ul:
        for li in ul.find_all('li'):
            img = li.find('img').get('src')
            name = li.find('p').text
            job = li.find('p', class_='regListJob').text
