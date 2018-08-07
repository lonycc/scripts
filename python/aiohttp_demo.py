# coding=utf-8

import asyncio
import aiohttp
from yarl import URL

async def main():
    async with aiohttp.ClientSession() as session:
        #async with session.get('http://httpbin.org/get', params={'k1': 'v1', 'k2': 'v2'}) as resp:
        #async with session.get('http://httpbin.org/get', params=[('k1', 'v1'), ('k1', 'v2')]) as resp:
        #async with session.get('http://httpbin.org/get', params='v+1') as resp:
        #async with session.get(URL('http://httpbin.org/get?%30', encoded=True)) as resp: #不再对url做编码处理
        #async with session.get('http://demo.com/xx.jpg') as resp:
        #async with session.post('http://httpbin.org/post', data=b'try_it_data') as resp: #上传bytes数据
        #async with session.post('http://httpbin.org/post', data={'k':'v'}) as resp: #上传form数据
        #async with session.post('http://httpbin.org/post', json={'k':'v'}) as resp: #上传json数据
        #async with session.post('http://httpbin.org/post', data={'file', open('xx.dat', 'rb'}) as resp: #上传文件
            # 状态码
            print(resp.status)
            
            # 仅限text类型资源
            print(await resp.text(encoding='utf-8'))
            
            # 仅限返回类型json
            print(await resp.json())
            
            # 写入二进制 response content
            with open(filename, 'wb') as fd:
                fd.write(await resp.read())
            
            # 二进制响应内容过大, 分块写入
            with open(filename, 'wb') as fd:
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    fd.write(chunk)


# 文件发送
async def file_sender(file_name=None):
    async with aiofiles.open(file_name, 'rb') as f:
        chunk = await f.read(64*1024)
        while chunk:
            yield chunk
            chunk = await f.read(64*1024)
            
# 上传文件/流
async def stream_uploads():
    async with aiohttp.ClientSession() as session:
        # 显示指定filename和content_type
        data = FormData()
        data.add_field('file', open('report.xls', 'rb'), filename='report.xls', content_type='application/vnd.ms-excel')
        await session.post('http://httpbin.org/post', data=data)
        
        # 大文件
        with open('bigtext.txt', 'rb') as f:
            await session.post('http://httpbin.org/post', data=f)
        
        # 流式发送大文件
        async with session.post('http://httpbin.org/post', data=file_sender(file_name='huge_file')) as resp:
            print(await resp.text())
        
        resp = await session.get('http://python.org')
        await session.post('http://httpbin.org/post', data=resp.content)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
