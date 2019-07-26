#!/usr/bin/env python3
# coding=utf-8

from requests import Session
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from urllib.request import urlopen
from json import loads, dumps
import time
import pymysql

mysql_config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'test',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}

mysql_conn = pymysql.connect(**mysql_config)
mysql_cur = mysql_conn.cursor()

session = Session()
stop_crawler = False
OOXX_MIN_ID = 4292527

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'jandan.net',
    'Origin': 'http://jandan.net',
    'Referer': 'http://jandan.net/ooxx',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def close_mysql():
    try:
        mysql_cur.close()
        mysql_conn.close()
    except Exception as e:
        print(e)

    
def guanren(start=60000, end=61000):
    for i in range(start, end, 1):
        url = 'https://www.guanren4.com/play/{}.html'.format(i)
        r = session.get(url, timeout=30)
        status_code = r.status_code
        if status_code == 200:
            soup = bs(r.text, 'html.parser')
            title = soup.find('div', class_='block_title')
            if title:
                title = title.text
                title = title.strip('[').replace(']', ' ')
                video_url = 'https://www.xunleibb.com/filets/{0}/list.m3u8'.format(i)
                print(f'[{title}]({video_url})\n')
        else:
            print(f'{url} not found')
    print('finished')

    
def jporn():
    for i in range(3011, 3050):
        url = 'http://jporn.link/units/{0}'.format(i)
        rs = session.get(url, headers=headers, timeout=10)
        soup = bs(rs.text, "html.parser")
        video = soup.find('source')
        if video:
            r = urlopen('http://jporn.link/units/{}/download'.format(i))
            name = r.info().get_filename()
            p = urljoin(url, video.get('src'))
            print(f'[{name}]({p})')
    print('finished')

    
def fuliba_list(start_url = 'http://fulibus.net/page/1'):
    r =  session.get(start_url, headers={}, timeout=10)
    if r.status_code == 200:
        soup = bs(r.text, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            h2 = article.find('h2').find('a')
            print(f'<p>{h2}</p>') 
   

def fuliba_tu(start=45, end=60):
    for i in range(start, end):
        url = 'http://fulibus.net/2019%03d.html/2' % i
        r =  session.get(url, headers={}, timeout=10)
        if r.status_code == 200:
            soup = bs(r.text, 'html.parser')
            article = soup.find('article', class_='article-content')
            for img in article.find_all('img'):
                print(f"![]({img.get('src')})")
                
def upload_sinaimg(url):
    r = session.get('https://api.yum6.cn/sinaimg.php', params={'img':url, '_': int(time.time())}, timeout=30)
    j = loads(r.text)
    if j['code'] == '200':
        print(j['url'].replace('/thumb150/', '/large/'))
        
# 1024
def t66y(url):
    r = session.get(url, timeout=6, proxies={'http': 'http://127.0.0.1:1087'})
    soup = bs(r.text, 'html.parser')
    content = soup.find('div', class_='tpc_content do_not_catch')
    for img in content.find_all('img'):
        url = img.get('data-src')
        print(f'![]({url})')
        #upload_sinaimg(url)
    print('finished')


# 豆瓣话题    
def douban_topic():
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
        r = session.get('https://m.douban.com/rexxar/api/v2/gallery/topic/57110/items', params=params, headers=headers)
        j = loads(r.text)
        for k in j['items']:
            if 'status' in k['target']:
                for img in k['target']['status']['images']:
                    print(f"![]({img['normal']['url']})")
            elif 'photos' in k['target']:
                for img in k['target']['photos']:
                    print(f"![]{img['src']}")

# 豆瓣图片专辑
def douban_album(start_url='https://www.douban.com/people/benbenbear/photos', cur_page=1, total_page=1):
    rs = session.get(start_url, headers={
        
    })
    soup = bs(rs.text, 'html.parser')
    albumlst = soup.find_all('div', class_='albumlst')
    for album in albumlst:
        album_title = album.find('div', class_='pl2').text.strip('\n')
        album_url = album.find('a', class_='album_photo').get('href')
        #print(f'[{album_title}]({album_url})')
        douban_photo(album_url)
        
    if cur_page == 1:
        count = soup.find('span', class_='count').text
        count_int = re.search(r'\d+', count)
        total_page = math.ceil(int(count_int.group())/18)
    if cur_page < total_page:
        start = cur_page * 18
        cur_page += 1
        douban_album(f'https://www.douban.com/people/benbenbear/photos?start={start}', cur_page, total_page)

# 豆瓣专辑列表
def douban_photo(album_url):
    rs = session.get(album_url, headers={})
    soup = bs(rs.text, 'html.parser')
    photos = soup.find_all('div', class_='photo_wrap')
    for photo in photos:
        photo_title = photo.find('div', class_='pl').text
        photo_url = photo.find('img').get('src')
        photo_url = photo_url.replace('/m/', '/l/')
        print(f'[{photo_title}]({photo_url})')
    
    next_page = soup.find('span', class_='next')
    if next_page and next_page.find('a'):
        douban_photo(next_page.find('a').get('href'))

# jandan list
def jandan_list(url):
    r = session.get(url, headers=headers, timeout=10)
    soup = bs(r.text, 'html.parser')
    next_page = soup.find('a', class_='previous-comment-page')
    jandan_img(soup)
    if next_page != None and stop_crawler == False:
        jandan_list(urljoin(url, next_page.get('href')))

# jandan img
def jandan_img(soup):
    global stop_crawler, OOXX_MIN_ID
    texts = soup.find_all('div', class_='text')
    for text in texts:
        spans = text.find_all('a', class_='view_img_link')
        id = text.find('span', class_='righttext').text
        if int(id) > OOXX_MIN_ID:
            for span in spans:
                href = span.get('href')
                if href.startswith('//'):
                    href = "https:{0}".format(href)
                sinaimg = href.replace('/mw600/', '/large/')
                print(sinaimg, id)
        else:
            print('done')
            stop_crawler = True
            break
