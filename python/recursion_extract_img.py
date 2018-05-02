#! /usr/bin/env python2.7
# coding=utf-8

import os
import sys
import re

try:
    from bs4 import BeautifulSoup
except ImportError as e:
    print('未安装bs4包, 请执行下面命令安装\npip install bs4')
    exit(0)


class Demo(object):
    def __init__(self, htmlPath, fileHandler, regText):
        self.htmlPath = htmlPath
        self.fileHandler = fileHandler
        self.regText = regText

    def readDir(self):
        '''
        遍历目录
        '''
        for dirpath, dirnames, filenames in os.walk(self.htmlPath):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                if re.search(self.regText, fullpath):
                    print(fullpath)
                    self.extractImg(fullpath)

    def extractImg(self, html_file):
        '''
        从html文件中解析正文部分<img>标签, 并写入文件中
        '''
        try:
            soup = BeautifulSoup(open(html_file, 'r', encoding='utf-8').read(), 'html.parser', from_encoding='utf-8')
            content_1 = soup.find('div', class_='content')
            content_2 = soup.find('div', class_='m-content')
            content_3 = soup.find('div', class_='articlebox')
            content = content_1
            if content_1 == None:
                content = content_2
                if content_2 == None:
                    content = content_3
            if content != None:
                imgs = content.find_all('img')
                for img in imgs:
                    try:
                        self.fileHandler.write(img.get('src')+'\n')
                    except:
                        pass
        except:
            print '%s may be wrong' % html_file
            pass

if __name__ == '__main__':
    regText_2018 = r'/20(0[0-9]|1[0-7])-\d{2}/\d{2}/content_.*\.htm$' #2018之前
    regText_2015 = r'/20(0[0-9]|1[0-4])-\d{2}/\d{2}/content_.*\.htm$' #2015之前
    regText_2012 = r'/20(0[0-9]|1[0-1])-\d{2}/\d{2}/content_.*\.htm$' #2012之前
    if len(sys.argv) < 3:
        print 'run this script like this: %s html_path file_to_save' % sys.argv[0]
        sys.exit(0)
    htmlPath = sys.argv[1]
    fileName = sys.argv[2]
    if not os.path.isdir(htmlPath):
        print '%s does not exist' % htmlPath
        sys.exit(0)
    if not os.path.isfile(fileName):
        print 'the result file %s not exists' % fileName
        sys.exit(0)
    with open(fileName, 'a+', encoding='utf-8') as fileHandler:
        demo = Demo(htmlPath, fileHandler, regText_2018)
        demo.readDir()
