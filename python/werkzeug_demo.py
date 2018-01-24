# coding=utf-8

from werkzeug.wrappers import Response,Request
from werkzeug.utils import escape
from werkzeug.serving import run_simple
from werkzeug.formparser import parse_form_data
from werkzeug.test import create_environ
import os
import sys

def application(environ, start_response):
	request = Request(environ)
	text = 'Hello %s' % request.args.get('name','tony')
	response = Response(text, mimetype='text/plain')
	return response(environ, start_response)

@Request.application
def demo(request):
	result = []
	if request.method == 'POST':
		result.append('<title>Greeter</title>')
	result.append('''
        <form action="" method="post">
            <p>Name: <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
	return Response(''.join(result), mimetype='text/html')

def demo2(environ, start_response):
	result = ['<title>Greeter</title>']
	if environ['REQUEST_METHOD'] == 'POST':
		form = parse_form_data(environ)[1]
		result.append('<h1>what %s!</h1>' % escape(form['name']))
	result.append('''
        <form action="" method="post">
            <p>Name: <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
	start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
	return [''.join(result)]
	
# WSGI Environment	
def test():
	environ = create_environ('/foo','http://localhost:2080/')
	environ['PATH_INFO']
	environ['SCRIPT_NAME']
	environ['SERVER_NAME']
	

def test2():
	from io import StringIO
	data = "name=this+is+encoded+form+data&another_key=another+one"
	request = Request.from_values(query_string='foo=bar&blah=blafasel',
		content_length=len(data), input_stream=StringIO(data),
		content_type='application/x-www-form-urlencoded',
		method='POST')
	print(request.method)
	print(list(request.args.keys()))
	print(request.args['blah'])
	request.form['name']

def store_file(request):
	file = request.files.get('my_file')
	if file:
		file.save('/home/log.txt')
	else:
		handle_the_error()

# enter Request
def test3():
	request = Request(environ)
	request.path
	request.host
	request.script_root
	request.url
	request.method

# Header Parsing
def test4():
	environ = create_environ()
	environ.update(
		HTTP_USER_AGENT='Mozilla/5.0 (Macintosh; U; Mac OS X 10.5; en-US; ) Firefox/3.1',
		HTTP_ACCEPT='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		HTTP_ACCEPT_LANGUAGE='de-at,en-us;q=0.8,en;q=0.5',
		HTTP_ACCEPT_ENCODING='gzip,deflate',
		HTTP_ACCEPT_CHARSET='ISO-8859-1,utf-8;q=0.7,*;q=0.7',
		HTTP_IF_MODIFIED_SINCE='Fri, 20 Feb 2009 10:10:25 GMT',
		HTTP_IF_NONE_MATCH='"e51c9-1e5d-46356dc86c640"',
		HTTP_CACHE_CONTROL='max-age=0'
	)
	request = Request(environ)
	print(request.cache_control.max_age)

# Responses
def app2(environ,start_response):
	response = Response('hi')
	#start_response('200 OK', [('Content-Type','text-plain')])
	#return ['test it']
	return response(environ,start_response)

def test5():
	response = Response('hi tony')
	response.headers['content-type']
	response.data
	response.headers['content-length'] = len(response.data)
	response.status
	response.status = '404 Not Found'  #modify the status
	response.status_code
	response.content-length
	from datetime import datetime
	response.date = datetime(2015, 6, 8, 15, 23, 44)
	response.headers['Date']   #set attributes
	response.set_etag('fasda-12332',weak=True)
	response.headers['etag']
	response.get_etag()
	response.content_language.add('en_us')  #language add
	response.content_language.add('en')
	response.headers['Content-Language']
	response.headers['Content-Language'] = 'de-AT, de'
	response.content_language
	response.www_authenticate.set_basic("my protected resource")
	response.headers['www-authenticate']
	response.www_authenticate
	response.set_cookie('name', 'value')   #set cookie
	response.headers['Set-Cookie']
	response.set_cookie('name2', 'value2')
	response.headers.getlist('Set-Cookie')  #get lists of cookie
		
	
if __name__ == '__main__':   
    run_simple('localhost', 4000, demo2)
	
