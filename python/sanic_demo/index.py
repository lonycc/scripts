# coding=utf-8

from sanic import Sanic, Blueprint
from sanic.response import json, html, text, redirect
from sanic.log import logger
from sanic.request import RequestParameters
from config import db_config
from functools import wraps

app = Sanic('myapp', strict_slashes=False)

app.static('/static', './static')
app.static('/uploads', './uploads', name='uploads')
app.static('/test.png', './test.png', name='test_png')

#app.url_for('static', filename='file.txt') == '/static/file.txt'
#app.url_for('static', name='static', filename='file.txt') == '/static/file.txt'
#app.url_for('static', name='uploads', filename='file.txt') == '/uploads/file.txt'
#app.url_for('static', name='test_png') == '/test.png'

blueprint = Blueprint('api', strict_slashes=False, url_prefix='api')

#app.config.update(db_config)

@blueprint.get('/bar', strict_slashes=False)
async def bar(request):
    return text(request.endpoint)

app.blueprint(blueprint)

@app.route('/', strict_slashes=False)
async def test(request):
    logger.info('request info')
    logger.error('request error')
    url = app.url_for('request_test', id=5, arg_one=['one', 'two'], arg_two=2, _anchor='anchor', _scheme='http', _external=True, _server='localhost:8000')
    # 如果路由有name属性, 则url_for第一个参数取name, 而非处理方法名
    return html(f'<h1>{url}</h1>')
    #return redirect(url)

@app.route('/get/<id:int>', methods=['GET'])
async def request_test(request, id):
    return json({
        "args": request.args,
        "url": request.url,
        "query_string": request.query_string,
        "raw_args": request.raw_args,
        'method': request.method,
        'ip': request.ip,
        'headers': request.headers,
        'endpoint': request.endpoint
    })

@app.route('/form', methods=['POST'], name='form')
async def form(request):
    return json({
        'form_data': request.form
    })

@app.route('/files', methods=['POST'])
async def files_upload(request):
    file = request.files.get('file')
    return json({
        'params': request.files.keys(),
        'body': file.body,
        'name': file.name,
        'type': file.type,
        'json': request.json,
        'request.body': request.body
    })

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

async def test_add_websocket_route(request, ws):
    pass

async def test_add_route(request, name):
    return text(name)

@app.middleware('request')
async def print_on_request(request):
    request['oo'] = 'xx'
    print('when a request is received')

@app.middleware('response')
async def print_on_response(request, response):
    response.headers['Server'] = 'South/1.5'
    response.headers['x-xss-protection'] = '1; mode=block'
    print('when a response is returned')

@app.middleware('request')
async def halt_request(request):
    return text('I halted the request')

@app.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')

@app.listener('before_server_start')
async def setup_db(app, loop):
    app.db = await db_setup()

@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server successfully started!')

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    print('Server shutting down!')

@app.listener('after_server_stop')
async def close_db(app, loop):
    await app.db.close()

async def notify_server_started_after_five_seconds(app):
    await asyncio.sleep(5)
    print(app.name)


def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authorized = check_login(request)
            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json({'status': 'not_authorized'}, 403)
        return decorated_function
    return decorator


async def check_login(request):
    return True


@app.route('/me')
@authorized()
async def meinfo(request):
    return json({'user': 'tony'}, status=403)

if __name__ == '__main__':
    #app.register_listener(setup_db, 'before_server_start')
    #app.add_task(notify_server_started_after_five_seconds)
    app.add_route(test_add_route, '/add/<name:str>', methods=['GET'])
    app.add_websocket_route(test_add_websocket_route, '/test_feed')
    app.run(host='127.0.0.1', port=8000, debug=True, access_log=False, auto_reload=True)
