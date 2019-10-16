**composer 用法**

`curl -sS https://getcomposer.org/installer | php` #下载composer.phar

或者也可以 

`php -r "readfile('https://getcomposer.org/installer');" | php`

> linux下，可以把composer.phar移动到/usr/bin目录下

> max下，可以把composer.phar移到/usr/local/bin目录下

> windows下，在composer.phar同级目录下新建composer.bat
`echo @php "%~dp0composer.phar" %*>composer.bat`
把composer.bat所在目录加入环境变量,即可使用composer命令


`composer init`  #初始化composer

`composer install`  #需要在当前目录下存在composer.json
```
composer.json
{
    "require": {
        "monolog/monolog": "1.0.*"
    }
}
```

`composer require slim/pdo "^1.9"`  #安装指定版本

`composer revomve [package]`  #移除包

`composer --no-dev update`  #更新包时删除无用包

`composer selfupdate` #更新composer

**配置中国全量镜像**

`composer config -g repo.packagist composer https://packagist.laravel-china.org`

**当前项目配置**
`composer config repo.packagist composer https://packagist.laravel-china.org`

**一些常用包**

`composer require samayo/bulletproof:2.0.*`  #图片上传

`composer require monolog/monolog`  #日志管理

`composer require tymon/jwt-auth`  #json web token 认证

`composer require nesbot/carbon`  #日期时间包

`composer require zhuzhichao/ip-location-zh`  #国人做的根据ip获取地名包

`composer require zizaco/entrust` #提供实现RBAC的包

`composer require simplesoftwareio/simple-qrcode` #简单二维码

`composer require predis/predis` #redis客户端

`composer require mews/purifier` #html标签过滤

`composer require summerblue/administrator` #一个laravel简单后台

`composer require maatwebsite/excel` #excel工具

`composer require intervention/image` #图像处理

`composer require dingo/api`  #api构建工具

<br/><br/>

**安装laravel**

`composer global require "laravel/installer"`

`/Users/work/.composer/vendor/bin/laravel new laravel5` #用laravel命令新建一个项目或者也可以

`composer create-project --prefer-dist laravel/laravel laravel5`

`composer create-project laravel/laravel blog 5.3.*`  #指定版本

**laravel 安装第三方服务步骤**

- 1.在程序根目录下执行`composer require memws/purifier`安装

- 2.在`config/app.php`中的`providers`中注册`ServiceProvider`, 在`aliases`中注册Facades

- 3.发布配置文件到`config`目录`php artisan vendor:publish`

`clean(Input::get('inputname'));`

`Purifier::clean(Input::get('inputname'));`

**辅助函数clean**
`clean('This is my H1 title', 'titles');`

`clean('This is my H1 title', array('Attr.EnableID' => true));`

**Facades提供的clean方法**
`Purifier::clean('This is my H1 title', 'titles');`

`Purifier::clean('This is my H1 title', array('Attr.EnableID' => true));`

**artisan 相关命令**

`php artisan make:middleware YourMiddle`

> 前置/后置, 区别在于运行在请求前/后.

> 注册Middleware, 在全局注册,`app/Http/Kernel.php`内`$middleware`数组定义.
为特殊路由指定,在`$routeMiddleware`数组定义.

`php artisan make:controller PhotoController [--resource] [--model=Photo]` #带--resource则生成资源控制器,--model参数会绑定模型

`php artisan make:auth` #创建auth模块

`php artisan make:model Client`  #新建App\Client.php

`php artisan make:migration create_sessions_table`或`php artisan session:table` #生成session表的迁移模型

`php artisan make:request StoreBlogPost`  #创建一个表单请求类

`php artisan down [--message='upgrading database'] [--retry=60]`  #进入维护状态

`php artisan up`  #停止维护

`php artisan config:cache` #将所有配置文件缓存到单个文件

`php artisan make:provider AppServiceProvider` #生成一个ServiceProvider

**laravel配置 `dingo/api` 和 `tymon/jwt-auth`**

**集成`dingo/api`**

> ①在composer.json的require字段中添加: `"dingo/api":"1.0.*@dev"`

> ②执行: `composer update`

> ③在config/app.php注册到providers数组:  `Dingo\Api\Provider\LaravelServiceProvider::class,`

> ④生成dingo配置文件config/api.php: `php artisan vendor:publish --provider="Dingo\Api\Provider\LaravelServiceProvider"`

> ⑤.env添加基础配置, 或者也可直接在api.php修改

> API_STANDARDS_TREE=vnd

> API_PREFIX=api

> API_VERSION=v1

> API_DEBUG=true

**集成`tymon/jwt-auth`**

> ①在composer.json的require字段中添加: `"tymon/jwt-auth":"0.5.*"`

> ②执行: `composer update`

> ③在config/app.php注册到providers数组:  `Tymon\JWTAuth\Providers\JWTAuthServiceProvider::class,`

> ④在config/app.php注册到aliases数组: `'JWTAuth'=> Tymon\JWTAuth\Facades\JWTAuth::class,` 和 `'JWTFactory'=> Tymon\JWTAuth\Facades\JWTFactory::class,`

> ⑤生成jwt配置文件config/jwt.php: `php aritsan vendor:publish --provider="Tymon\JWTAuth\Providers\JWTAuthServiceProvider"`

> ⑥生成jwt.php文件中的secret键对应的值: `php aritsan jwt:generate`

**关联api和jwt-auth**

修改`config/api.php`的`auth`数组如下:

```
'auth' => [  
    'basic' => function($app){  
        return new Dingo\Api\Auth\Provider\Basic($app['auth']);  
    },  
    'jwt' => function($app){  
        return new Dingo\Api\Auth\Provider\JWT($app['Tymon\JWTAuth\JWTAuth']);  
    }  
],
```

**路由**

```
Route::get('/', function () {
    return view('home');  //返回视图
    return 'hello demo';   //返回字符串
    return ['name'=>'tony', 'age'=>26];   //返回数组, 会自动转为json格式字符串
    return response('Hello World', 200)->header('Content-Type', 'text/plain');  //自定义响应头, header方法可链式
    return redirect('/home/dashboard');  //重定向
    return back()->withInput();  //提交失败返回, 表单保持
    return redirect()->route('login');  //重定向至命名路由
    return redirect()->route('profile', ['id' => 1]);  //带参数
    return redirect()->route('profile', [$user]);   //Eloquent模型填充参数
    return redirect()->action('HomeController@index');  //重定向至路由行为
    return redirect()->action('HomeController@index', ['id' => 1]);
    return redirect('dashboard')->with('status', 'Profile updated!'); //附加session闪存数据, 可取出展示在模板
    return response()->view('hello', $data, 200)->header('Content-Type', $type);  //视图响应
    return response()->json([
        'name' => 'tony',
        'age' => 25,
    ]);
});

Route::get('post/create', 'PostController@create'); //GET路由$errors会被自动绑定
Route::post('post', 'PostController@store');


// get和post, 但要注意post方法有csrf保护
Route::match(['get', 'post'], 'fuck', function () {
    return 'you can fuck via get or post method';
});

// 任意动作
Route::any('fuck2', function () {
    return 'you can fuck2 via all http method';
});

// 必选参数
Route::get('user/{id}', function ($id) {
    return "user: {$id}";
});

Route::get('posts/{post}/comments/{comment}', function ($postId, $commentId) {
    return "posts: {$postId}, comments: {$commentId}";
});

// 可选参数
Route::get('user2/{name?}', function ($name = null) {
    return $name;
});

Route::get('user3/{name?}', function ($name = 'John') {
    return $name;
});

// 正则约束
Route::get('user4/{name}', function ($name) {
    return "user4/{name} and name must be english chars {$name}";
})->where('name', '[A-Za-z]+');

Route::get('user5/{id}', function ($id) {
    
})->where('id', '[0-9]+');

Route::get('user6/{id}/{name}', function ($id, $name) {
    
})->where(['id' => '[0-9]+', 'name' => '[a-z]+']);

// 命名路由, 生成URL或重定向到指定的路由
Route::get('user7/profile', function () {
    return 'this is user/profile';
})->name('profile');

//$url = $route('profile'); //生成url
//return redirect()->route('profile'); //生成重定向

// 为控制器方法指定路由名称
Route::get('user8/profile', 'UserController@showProfile')->name('profile1');

// 带参数命名路由
Route::get('user9/{$id}/profile', function ($id) {
    
})->name('profile2');

$url = route('profile2', ['id' => 1]);


// 路由组, 共享路由属性如middleware/namespace/domain/prefix
Route::group(['middleware' => ['auth', 'session']], function () {
    Route::get('/fuck3', function () {
        
    });
    Route::get('/fuck4', function () {
        
    });
});

// 路由模型绑定
Route::get('api/users/{user}', function (App\User $user) {
    return $user->email;
});

// 分配middleware, 需要先在app/Http/Kernel.php中添加先
Route::get('admin/profile', function () {
    //
})->middleware('auth', 'second');
//use App\Http\Middleware\Check
//middleware(Check::class);

// $middlewareGroups, 开箱即用的`web`中间件组被自动用于`RouteServiceProvider`中定义的`routes/web.php`
Route::get('what/fuck', function () {
    //
})->middleware('web');

Route::group(['middleware' => ['web']], function () {
    //
});

// 中间件带参数
Route::put('post/{id}', function ($id) {
    //
})->middleware('role:editor');

// 在控制器的构造方法中指定中间件更便捷
Route::get('profile', 'UserController@show')->middleware('auth');

// 资源路由
Route::resource('photo', 'PhotoController');


// 部分资源路由
Route::resource('photo', 'PhotoController', ['only' => [
    'index', 'show'
]]);

Route::resource('photo', 'PhotoController', ['except' => [
    'create', 'store', 'update', 'destroy'
]]);

// 命名资源路由
Route::resource('photo', 'PhotoController', ['names' => [
    'create' => 'photo.build'
]]);

// 命名资源路由参数, /user/{admin_user}
Route::resource('user', 'AdminUserController', ['parameters' => [
    'user' => 'admin_user'
]]);
Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');

// 路由闭包获取请求
Route::get('/home', function (Illuminate\Http\Request $request) {
    //
});
```

`Route::get('articles',['uses'=>'ArticlesController@index', 'as'=>'articles.index']);`   访问`http://localhost/articles`

**在模板中生成链接, 有如下方式:**

- 1. 简单模式

`<a href="{{ url('/articles') }}">链接</a>`  或 `<a href="{{ URL::to('/articles') }}">链接</a>`

- 2. 路由模式

`URL::route('articles.index)`

- 3. 控制器动作模式

`URL::action('ArticlesController@index')`

`Route::controller('users', 'UsersController');`  //会生成rest风格路由

**命名路由**

1. 通过route路由中的as关键字实现

`Route::get('api/user', ['as'=>'web.user'], 'messageController@user');`

2. 通过Route的magic方法name来实现命名路由

`Route::get('api/user', 'messageController@user')->name('web.user');`

代码中可以`$this->visit(route('web.user'));`; 在模板中`<a href="{{route('web.user')}}">user</a>`


**laravel 获取上次执行的sql语句的主键id**

$id = DB::getPdo()->lastInsertId();

或者指定id
$id = DB::table('tb_name')->insertGetId(['id'=>10, 'name'=>'tony']);  //返回10

**laravel+nginx**

```
server {
    listen 80;
    server_name example.com;
    root /example.com/public;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";

    index index.html index.htm index.php;

    charset utf-8;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location = /favicon.ico { access_log off; log_not_found off; }
    location = /robots.txt  { access_log off; log_not_found off; }

    error_page 404 /index.php;

    location ~ \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/var/run/php/php7.1-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
}
```
**laravel优化**

`composer install --optimize-autoloader`

`php artisan config:cache`

`php artisan route:cache`

**docker容器化部署laravel项目**

`docker run -d --name php7.1 -p 80:80 -p 443:443 -v /path/to/project_name:/var/www/html/project_name richarvey/nginx-php-fpm:latest`

**alpine中安装php扩展ldap**

[alpine仓库](http://dl-3.alpinelinux.org/alpine/)

[alpine pkgs](https://pkgs.alpinelinux.org/packages)

[alpine wiki](http://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)

`apk add --no-cache pkg_name`

`apk add openldap --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/main/ --allow-untrusted`

`apk add openldap-dev --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/main/ --allow-untrusted`

```
apk add --no-cache openldap
apk add --no-cache openldap-dev
/usr/local/bin/docker-php-ext-configure ldap
/usr/local/bin/docker-php-ext-install ldap
/usr/local/bin/docker-php-ext-enable ldap
```

**laravel 内部调用**

```
    public function index(Request $request)
    {
        $request->request->add([
            'access_token' => 'abcd',
        ]);

        $proxy = Request::create(
            'api/oauth/info',
            'POST'
        );

        $response = \Route::dispatch($proxy);
        return $response;
    }
```

**laravel修改$request**
```
$input = $request->all();
array_walk_recursive($input, function (&$input) {
    $input = "<pre>{$input}</pre>";
});
$request->replace($input);
dd($request->all());
```



**laravel多线程连接数据库带来的问题(封装的mysql/redis都是单例模式)**

```
mysql
DB::purge('mysql');
DB::reconnect('mysql');

redis
$redis = new \Redis();
$re1 = $redis->connect(env('REDIS_HOST'), env('REDIS_PORT'));
$re2 = $redis->auth(env('REDIS_PASSWORD'));

for ($i=0; $i<5; $i++) {
    $pid = pcntl_fork();
    if ( $pid == -1 ) {
        echo 'fork thread failed' . PHP_EOL;
    } else if ( $pid ) {
        echo "fork succeed, pid={$pid}" . PHP_EOL;
    } else {
        echo $i . PHP_EOL;
        exit(0);
    }
}

while ( pcntl_waitpid(0, $status) != -1 ) {
    $status = pcntl_wexitstatus($status);
    $pid = posix_getpid();
    echo "{$status} -- {$pid}" . PHP_EOL;
}
```
