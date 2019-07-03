**参考资料**

[中文文档](https://www.yuanrenxue.com/sanic/sanic-start.html)

[官方文档](https://sanic.readthedocs.io/en/latest/sanic/getting_started.html)

**request**


**response**

```
from sanic.reponse import html, text, json, file, stream, file_stream, redirect, raw

@app.route('/response')
async def test(request):
    return html('<h3>html response</h3>')
    return text('text response')
    return json({'data': 'json response'}, headers={}, status=200)
    return file('/var/www/abc.jpg')
    return await file_stream('/var/www/abc.jpg')
    return redirect('/api/test')
    return raw(b'raw data')
    return stream(stream_fn, content-type='text/plain')
```


**cookie**

```
@app.route("/cookie")
async def test(request):
    value = request.cookies.get('key')  # 读取
    response = text('test cookie')
    response.cookies['key'] = 'value'  # 设置
    response.cookies['key']['domain'] = '.test.com'
    response.cookies['key']['httponly'] = True
    del response.cookies['key']   # 删除
    return response
```

**exception**

```
from sanic import Sanic
from sanic.exceptions import ServerError, bort, NotFound
from sanic.response import text, json
from sanic.handlers import ErrorHandler

async def server_error_handler(request, exception):
    return json({}, status=500)

# 通用错误处理类
class CustomErrorHandler(ErrorHandler):
    def default(self, request, exception):
        ''' 处理未被分配错误处理器的错误 '''
        # todo通用错误处理业务逻辑代码
        return super().default(request, exception)
        
app = Sanic()
app.error_handler.add(Exception, server_error_handler)  # 全局异常处理
# app.error_handler = CustomErrorHandler()

@app.route('/killme')
async def i_am_ready_to_die(request):
    raise ServerError('server error', status_code=500)
    
@app.route('/youshallnotpass')
async def no_no(request):
    abort(401)   # 直接抛出401异常, 下面的代码不会执行
    text('h')
    
@app.exception(NotFound)  # 自定义异常处理, 覆盖默认的
async def ignore_404s(request, exception):
    return json({'errcode': 404, 'errmsg': f'{request.url} not found'}, status=200)
```

**version**

```
@app.route("/text", version=1)  # 对应的路由/v1/text
async def test(request):
    return text('Hi, Version 1\n')

@app.route("/text", version=2)  # 对应路由/v2/text
async def test(request):
    return text('Hi, Version 2\n')


bp = Blueprint('test', version=1)  # 蓝图加版本控制

@bp.route('/html')  # 对应路由 /v1/html
def handle_request(request):
    return response.html('<p>Hello world!</p>')
```

**websocket**

```
from sanic import Sanic
from sanic.response import json
from sanic.websocket import WebSocketProtocol

app = Sanic()

# websocket相关配置参数
app.config.WEBSOCKET_MAX_SIZE = 2 ** 20
app.config.WEBSOCKET_MAX_QUEUE = 32
app.config.WEBSOCKET_READ_LIMIT = 2 ** 16
app.config.WEBSOCKET_WRITE_LIMIT = 2 ** 16

@app.websocket('/feed')  # websocket装饰器
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

async def feed(request, ws):
    pass

app.add_websocket_route(feed, '/test_feed')  # 支持两种方法添加websocket路由

app.run(host='0.0.0.0', port=8000, protocol=WebSocketProtocol)  # 显示声明仅支持ws协议
```

**handler decorator**

```
from functools import wraps
from sanic.response import json

def logined():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_logined = check_login(request)
            if is_logined:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json({'status': 'not login'}, 403)
        return decorated_function
    return decorator

async def check_login(request):
    return True

@app.route("/")
@logined()  # 添加登陆检查装饰器, 检查是否登陆
async def test(request):
    return json({'status': 'logined'})
```

**stream 流式请求/响应/文件**

```
from sanic import Sanic
from sanic.views import CompositionView
from sanic.views import HTTPMethodView
from sanic.views import stream as stream_decorator
from sanic.blueprints import Blueprint
from sanic.response import stream, text, file_stream
from aiofiles import os as async_os

bp = Blueprint('blueprint_request_stream')
app = Sanic(__name__)


class SimpleView(HTTPMethodView):
    @stream_decorator
    async def post(self, request):
        result = ''
        while True:
            body = await request.stream.read()
            if body is None:
                break
            result += body.decode('utf-8')
        return text(result)


@app.post('/stream', stream=True)  # curl -XPOST /stream
async def handler(request):
    async def streaming(response):
        while True:
            body = await request.stream.read()
            if body is None:
                break
            body = body.decode('utf-8').replace('1', 'A')
            await response.write(body)
    return stream(streaming)


@bp.put('/bp_stream', stream=True)
async def bp_put_handler(request):
    result = ''
    while True:
        body = await request.stream.read()
        if body is None:
            break
        result += body.decode('utf-8').replace('1', 'A')
    return text(result)



async def bp_post_handler(request):
    result = ''
    while True:
        body = await request.stream.read()
        if body is None:
            break
        result += body.decode('utf-8').replace('1', 'A')
    return text(result)

bp.add_route(bp_post_handler, '/bp_stream', methods=['POST'], stream=True)


async def post_handler(request):
    result = ''
    while True:
        body = await request.stream.read()
        if body is None:
            break
        result += body.decode('utf-8')
    return text(result)

app.blueprint(bp)
app.add_route(SimpleView.as_view(), '/method_view')
view = CompositionView()
view.add(['POST'], post_handler, stream=True)
app.add_route(view, '/composition_view')


@app.route('/response')
async def test(request):  # 流式响应
    async def sample_streaming_fn(response):
        await response.write('foo,')
        await response.write('bar')
    return stream(sample_streaming_fn, content_type='text/csv')

@app.route('/file')
async def index(request):
    file_path = "/var/www/test.tar.gz"
    file_stat = await async_os.stat(file_path)
    headers = {"Content-Length": str(file_stat.st_size)}

    return await file_stream(
        file_path,
        headers=headers,
        chunked=True,
        status=200,
        chunk_size=4096,
        filename='test.tar.gz',
        mime-type='application/gzip',
    )
```

**基于类的视图**

```
from sanic import Sanic
from sanic.views import HTTPMethodView, CompositionView
from sanic.response import text

app = Sanic('some_name')

class SimpleView(HTTPMethodView):
    decorators = [common_decorator]  # 通用装饰器
    
    async def get(self, request, name):
        return text(f'get {name}')

    def post(self, request, name):
        return text('I am post method')

    @decorator_put  # 只对put方法
    def put(self, request):
        return text('I am put method')

    def patch(self, request):
        return text('I am patch method')

    def delete(self, request):
        return text('I am delete method')

app.add_route(SimpleView.as_view(), '/<name:str>')  # 参数仅支持接收参数的方法, 本例中为get/post

app.url_for('SimpleView')  # 获取基于类的视图的url, 参数传递类名

def get_handler(request):
    return text('test get handler')

view = CompositionView()
view.add(['GET'], get_handler)
view.add(['POST', 'PUT'], lambda request: text('I am a post/put method'))
app.add_route(view, '/compositionview')
```
