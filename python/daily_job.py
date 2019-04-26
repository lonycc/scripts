#!/usr/bin/env python3
# coding=utf-8

from requests import Session
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from urllib.request import urlopen
from json import loads, dumps
import time

s = Session()
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
post_headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': 136,
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'jandan.net',
'Origin': 'http://jandan.net',
'Referer': 'http://jandan.net/ooxx',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

def jandan_comment():
    data = {
        'author': 'zoo',
        'email': 'zoo@zoo.zoo',
        'comment': 'https://ws1.sinaimg.cn/large/007awY0bly1fzbu58fadjj30m80xcqar.jpg',
        'comment_post_ID': 21183
    }
    post_headers['Content-Length'] = str(len(dumps(data)))
    r = s.post('http://jandan.net/jandan-comment.php', 
           data=data, 
           headers=post_headers, 
           timeout=30)
    print(r.text)

def guanren(start=42219, end=42250):
    fs = open('p.md', 'a+')
    for i in range(start, end):
        url = 'https://www.guanren4.com/play/{}.html'.format(i)
        print(i)
        r = s.get(url, timeout=30)
        soup = bs(r.text, 'html.parser')
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
            r = urlopen('http://jporn.link/units/{}/download'.format(i))
            name = r.info().get_filename()
            p = urljoin(url, video.get('src'))
            print(f'[{name}]({p})')
    print('finished')

def fuliba_list(start_url = 'http://fulibus.net/page/1'):
    r =  s.get(start_url, headers={}, timeout=10)
    if r.status_code == 200:
        soup = bs(r.text, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            h2 = article.find('h2').find('a')
            print(f'<p>{h2}</p>') 
                
def fuliba_tu(start=45, end=60):
    for i in range(start, end):
        url = 'http://fulibus.net/2019%03d.html/2' % i
        r =  s.get(url, headers={}, timeout=10)
        if r.status_code == 200:
            soup = bs(r.text, 'html.parser')
            article = soup.find('article', class_='article-content')
            for img in article.find_all('img'):
                print(f"![]({img.get('src')})")
                
def upload_sinaimg(url):
    r = s.get('https://api.yum6.cn/sinaimg.php', params={'img':url, '_': int(time.time())}, timeout=30)
    j = loads(r.text)
    if j['code'] == '200':
        print(j['url'].replace('/thumb150/', '/large/'))
        
        
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
        url = img.get('data-src')
        print(f'![]({url})')
        #upload_sinaimg(url)
    print('finished')

def douban():
     params = {
        'sort': 'hot',
        'start': 0,
        'count':20,
        'status_full_text':1,
        'guest_only':0,
        'ck':'null'
    }
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.douban.com',
    'Referer': 'https://www.douban.com/gallery/topic/57110/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.3 Safari/537.36'
    }
    for i in range(0, 24):
        print(i)
        params['start'] = i * 20
        r = s.get('https://m.douban.com/rexxar/api/v2/gallery/topic/57110/items', params=params, headers=headers)
        j = loads(r.text)
        for k in j['items']:
            if 'status' in k['target']:
                for img in k['target']['status']['images']:
                    print(f"![]({img['normal']['url']})")
            elif 'photos' in k['target']:
                for img in k['target']['photos']:
                    print(f"![]{img['src']}")
                    
