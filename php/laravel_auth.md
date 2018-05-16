**用户认证**

config/auth.php

```
guard (看守器)
guards.web.driver session
guards.api.driver token
guards.api.driver passport
guards.web.provider users (这里可自定义名字)
guards.api.provider users


provider (提供器)
providers.users.driver eloquent
providers.users.model App\User::class

providers.users.driver database
providers.users.table xxx
```


快速生成身份验证所需路由和视图
`php artisan make:auth`

自定义`guard`, 在`App\Http\Controllers\Auth`命名空间里
`LoginController` / `RegisterController` / `ResetPasswordController`中定义`guard`方法, 返回一个`gurad`实例:

```
use Illuminate\Support\Facades\Auth;

protected function guard()
{
    return Auth::guard('guard-name');
}
```

自定义验证/存储, 可以在`RegisterController`里修改`validator`方法.

检索认证用户, 用 `Auth` facade 访问: `Auth::user();` / `Auth::id();`, 或者利用`Illuminate\Http\Request`实例来访问`$request->user();`.

确认当前用户是否认证, 用 `Auth::check();`.

保护路由, 只需对路由加上中间件, `Route::get('profile', function() {})->middleware('auth');`; 如果在控制器中, 则只需在其构造方法中调用`$this->middleware('auth');`.

指定guard, 将auth中间件添加到路由时, 还需指定guard, 例如
`$this->middleware('auth:api');`, 表示适用于api的guard.

登录限制, `LoginController` 包含了 `Illuminate\Foundation\Auth\ThrottlesLogins` trait, 默认多次尝试认证失败会被限制;

手动认证用户, 通过 `Auth` facade 来访问Laravel的认证服务, 然后使用 `attempt` 方法, `Auth::attempt(request('email', 'password)); redirect()->intended('dashboard);`

访问指定的guard实例, 通过 `Auth` facade 的 `guard` 方法指定要使用的guard实例. 

```
if ( Auth::guard('admin')->attempt($credentials) ) {
	//
}
```

注销用户`Auth::logout();`

记住用户`Auth::attempt(['email' => $email, 'password' => $password], $remember);`, 通过`Auth::viaRemember();`检查用户是否使用[记住我] cookie进行认证;

`Auth::login($user);` //登录用户

`Auth::login($user, true);`  //登录并记住用户

`Auth::guard('admin')->login($user);`

`Auth::loginUsingId(1);`  //通过id验证用户

`Auth::loginUsingId(1, true);`  //登录并记住用户

`Auth::once($credentials);`  //仅验证用户一次, 不使用session/cookies


**laravel/passport实现的oauth2授权认证**

- 安装`composer require laravel/passport`

- 数据库迁移`php artisan migrate`

- 生成密钥和客户端`php artisan passport:install`

- 配置`config/auth.php`, `guards.api.driver=passport`

- 修改`app/Providers/AuthServiceProvider.php`, 新增内容如下:

```
use Laravel\Passport\Passport;
use Carbon\Carbon;

class AuthServiceProvider extends ServiceProvider
{
    public function boot()
    {
        $this->registerPolicies();

        //
        Passport::routes();
        Passport::tokensCan([
            'conference' => '请求访问您的个人信息'
        ]);
        Passport::tokensExpireIn(Carbon::now()->addMinute(100));
        Passport::refreshTokensExpireIn(Carbon::now()->addDays(30));
    }
}
```

- `routes/api.php` 如下:

```
Route::post('/login', 'DemoController@login')->name('login.login');
Route::post('/logout', 'DemoController@logout')->name('login.logout');
Route::post('/refresh', 'DemoController@refresh')->name('login.refresh');
Route::post('/register', 'DemoController@register')->name('login.register');
Route::middleware('auth:api')->group(function () {
    Route::get('/user', function (Request $request) {
        return $request->user();
    });
});

Route::get('/token', 'DemoController@token')->name('login.token');
```

- `app/Http/Controllers/DemoController.php` 如下:

```
<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\AuthenticatesUsers;
use Illuminate\Support\Facades\Auth;
use Laravel\Passport\Client;
use Illuminate\Http\Request;
use Validator;


class DemoController extends Controller
{
    use AuthenticatesUsers;

    public function __construct()
    {
        $this->middleware('auth:api')->only(['logout']);
    }

    /**
     * 登录, 密码模式认证授权
     */
    public function login(Request $request)
    {
        $credentials = $request->only('email', 'password');
        $remember_me = $request->has('remember') ? true : false;
        if ( $this->guard('api')->attempt($credentials, $remember_me) )
        {
            $this->clearLoginAttempts($request);
            $password_client = Client::query()->where('password_client', 1)->latest()->first();
    
            $request->request->add([
                'grant_type' => 'password',
                'client_id' => $password_client->id,
                'client_secret' => $password_client->secret,
                'username' => $credentials['email'],
                'password' => $credentials['password'],
                'scope' => ''
            ]);
    
            $proxy = Request::create(
                'oauth/token',
                'POST'
            );
    
            $response = \Route::dispatch($proxy);
            return ['code' => 200, 'data' => json_decode($response->original, true)];
        }
        return ['code' => 401, 'message' => '授权失败'];
    }

    /**
     * 注销令牌
     */
    public function logout(Request $request)
    {
        if ( Auth::guard('api')->check() )
        {
            Auth::guard('api')->user()->token()->revoke();
        }
        return ['code' => 200, 'message' => '注销成功'];
    }

    /**
     * 更新令牌
     */
    public function refresh(Request $request)
    {
        $password_client = Client::query()->where('password_client', 1)->latest()->first();
        $refresh_token = $request->has('refresh_token') ? $request->get('refresh_token') : '';

        $request->request->add([
            'refresh_token' => $refresh_token,
            'grant_type' => 'refresh_token',
            'client_id' => $password_client->id,
            'client_secret' => $password_client->secret,
            'scope' => '',
        ]);
        
        $proxy = Request::create(
            'oauth/token',
            'POST'
        );

        $response = \Route::dispatch($proxy);
        if ( array_key_exists('message', json_decode($response->original, true)) )
        {
            return ['code' => 401, 'data' => json_decode($response->original, true)];
        }
        return ['code' => 200, 'data' => json_decode($response->original, true)];
    }

    /**
     * 创建个人访问token， 该token永久有效
     */
    public function token()
    {
        $user = \App\Models\User::find(1);
        $token = $user->createToken('ptoken')->accessToken;
        // $token = $user->createToken('My Token', ['place-orders'])->accessToken;
        return $token;
    }

    /**
     * 注册后自动生成token
     */
    public function register(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'name'    => 'required|unique:users',
            'email' => 'required|unique:users',
            'password' => 'required|between:8,32',
        ]);

        if ( $validator->fails() )
        {
            return ['code' => 401, 'message' => $validator->errors()->toArray()];
        }

        $client = Client::query()->where('password_client', 1)->latest()->first();
        $request->request->add([
            'grant_type' => 'password',
            'client_id' => $client->id,
            'client_secret' => $client->secret,
            'username' => $request->email,
            'password' => $request->password,
            'scope' => ''
        ]);

        $proxy = Request::create(
            'oauth/token',
            'POST'
        );

        $response = \Route::dispatch($proxy);
        return ['code' => 200, 'data' => json_decode($response->original, true)];
    }

}
```
