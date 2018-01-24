#!/usr/bin/python
#coding=utf-8
import re
import sys
import os
import io
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
from collections import deque
import zlib
import time
import socket
socket.defaulttimeout = 5
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


class Crawler(object):
	def __init__(self, filename):
		self.logfile = open(filename, 'a+')
		self.entry = 'http://www.people.com.cn/'
		self.today = time.strftime('%Y/%m%d')
		self.yesterday = time.strftime('%Y/%m%d', time.localtime(time.time()-24*60*60))
		self.reg_url = '(?<=href=[\'"]).*?(?=[\'"])'

	def craw(self):
		qdetail = set()
		qnode = deque()
		qnode.append(self.entry)
		Anode = {self.entry}
		reg_detail = r'http://[\w\d]{1,20}\.people.com.cn/n1\d{1}/('+self.today+'|'+self.yesterday+')/c\d+\-\d+\.html$'
		reg_node = r'http://[\w\d]{1,20}\.people.com.cn/[^.#:\?]*$'
		reg_node_2 = r'http://[\w\d]{1,20}\.people.com.cn/[^.]*/(index|index\d{1})\.html$'
		while qnode:
			url = qnode.popleft()
			try:
				print( 'remain %d' % (len(qnode)) )
				html = self.getHtml(url, self.entry, 'www.people.com.cn')
				re_obj = re.compile(self.reg_url)
				urllist = re_obj.findall(html)
			except Exception as e:
				print('something wrong', e)
				pass
			else:
				for x in urllist:
					url_x = urllib.parse.urljoin(url, x)
					if re.match(reg_detail, url_x) and url_x not in qdetail:
						qdetail |= {url_x}
						self.logfile.write(url_x+'\n')
					elif (re.match(reg_node, url_x) or re.match(reg_node_2, url_x)) and url_x not in Anode:
						Anode |= {url_x}
						qnode.append(url_x)
					else:
						pass
			time.sleep(0.1)
		self.logfile.close()
		print("finished")

	# 源码获取
	def getHtml(self, url, referer='https://www.baidu.com', host='www.baidu.com', decoding='utf-8'):
		cookie_support = urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
		opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
		urllib.request.install_opener(opener)
		opener.addheaders = [('User-agent','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),('Accept','*/*'),('Referer',referer),('Host',host)]
		page = opener.open(url, timeout=5)
		buf = page.read()
		charset = page.info().get_content_charset()
		if page.info().get('Content-Encoding'):
			if 'gzip' in page.info().get('Content-Encoding'):
				html = zlib.decompress(buf, 16+zlib.MAX_WBITS)
		else:
			html = buf
		opener.close()
		#result = chardet.detect(html)
		if charset is not None:
			return html.decode(charset)
		elif b'charset=gb2312' in html:
			return html.decode('gb2312')
		elif b'charset=GB2312' in html:
			return html.decode('gb2312')
		elif b'charset=GBK' in html:
			return html.decode('gbk')
		else:
			return html.decode(decoding)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('usage: python '+sys.argv[0]+' /save/to/file')
		sys.exit(0)

	if not os.path.exists(sys.argv[1]):
		print(sys.argv[1] + ' is not exists')
		sys.exit(0)

	c = Crawler(sys.argv[1])
	c.craw()
