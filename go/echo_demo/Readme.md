**echo框架入门介绍和使用demo**

> echo框架相当轻量, 核心只提供了http请求处理、路由配置以及中间件使用.ORM、RPC之类都由第三方包提供, 有很大的灵活性.

**中间件**

- 在路由处理request之前, 可用于修改request属性, `Echo.Pre()`

HTTPSRedirect / HTTPSWWWRedirect / WWWRedirect / NonWWWRedirect / AddTrailingSlash / RemoveTrailingSlash / MethodOverride / Rewrite

- 在路由处理之后, 可访问Echo.Context所有接口, `Echo.Use()`

BodyLimit / Logger / Gzip / Recover / BasicAuth / JWTAuth / Secure / CORS / Static

- 路由组使用

`admin := e.Group("/admin", middleware.BasicAuth())` 或 `admin.Use()`

- 路由级别的中间件

`e.GET("/", <Handler>, <Middleware...>)`

- 跳过中间件

需要定义一个Skipper方法

**Basic Auth Middleware**

> http基础认证中间件, 凭证可用则继续下一步处理; 凭证无效则发送401响应.

可以是闭包实现的方法

```
e.Use(middleware.BasicAuth(func(username, password string, c echo.Context) (bool, error) {
	if username == "joe" && password == "secret" {
		return true, nil
	}
	return false, nil
}))
```

或者结构体实现

```
func validatorFunc(username, password string, c echo.Context) (bool, error) {
  if username == "tony" && password == "123456" {
    return true, nil
  }
  return false, nil
}

e.Use((middlewaremiddle.BasicAuthWithConfig(middleware.BasicAuthConfig{
  Skipper: nil,
  Validator: validatorFunc,
  Realm: "Restricted",
}))
```

**Body Dump Middleware**

> 该中间件获取请求和响应体并调用注册的处理函数, 通常用于调试和日志目的.

```
e.Use(middleware.BodyDump(func(c echo.Context, reqBody, resBody []byte) {
}))
```
或者
```
func BodyDumpHandler(echo.Context, []byte, []byte) {
}

e.Use(middleware.BodyDumpWithConfig(middleware.BodyDumpConfig{
  Skipper: nil,
  Handler: BodyDumpHandler,
}))
```

**Body Limit Middleware**

> 该中间件设置最大允许request body, 如果超出则返回413响应;

`e.Use(middleware.BodyLimit("2M"))` //可选单位K/M/G/T/P

```go
e.Use(middleware.BodyLimitWithConfig(middleware.BodyLimitConfig{
  Skipper: nil,
  Limit: "10MB",
}))
```

**CORS Middleware**

> 该中间件实现跨域资源的请求.

`e.Use(middleware.CORS())`
或者
```
e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
  Skipper: nil,
  AllowOrigins: []string{"https://labstack.com", "https://labstack.net"},
  AllowHeaders: []string{echo.HeaderOrigin, echo.HeaderContentType, echo.HeaderAccept},
  AllowCredentials: false,
  ExposeHeaders: []string{},
  MaxAge: 3600,
}))
```

**CSRF Middleware**

> 该中间件提供跨站请求伪造保护

`e.Use(middleware.CSRF())`
或
```
e.Use(middleware.CSRFWithConfig(middleware.CSRFConfig{
  Skipper: nil,
  TokenLength: 32,
  TokenLookup: "header:X-XSRF-TOKEN",
  ContextKey: "csrf",
  CookieName: "_csrf",
  CookieDomain: nil,
  CookiePath: nil,
  CookieMaxAge: 86400,
  CookieSecure: false,
  CookieHTTPOnly: false,
}))
```

**JWT Middleware**

> 该中间件提供jwt认证; token有效则把用户置于上下文并进行下一步处理; token无效则返回401; 无token或Authorization头无效则返回400;

`e.Use(middleware.JWT([]byte("secret")))`
或
```
e.Use(middleware.JWTWithConfig(middleware.JWTConfig{
  Skipper: nil,
  SigningKey: []byte("secret"),
  SigningMethod: "HS256",
  ContextKey: "user",
  Claims: jwt.MapClaims{},
  TokenLookup: "query:token",
  AuthScheme: "Bearer",
}))
```

**Logger Middleware**

> 日志中间件记录每个http请求的信息

`e.Use(middleware.Logger())`
或
```go
e.Use(middleware.LoggerWithConfig(middleware.LoggerConfig{
  Skipper: nil,
  Format: "time=${time_unix}, user_agent=${user_agent}, method=${method}, uri=${uri}, status=${status}\n",
  Output: os,Stdout,
}))
```

**Method Override Middleware**

> 方法重载中间件, 只有POST方法可以被重载.

`e.Pre(middleware.MethodOverride())`
或
```
e.Pre(middleware.MethodOverrideWithConfig(middleware.MethodOverrideConfig{
  Skipper: nil,
  Getter: middleware.MethodFromForm("_method"),
}))
```

**Proxy Middleware**

> 代理中间件提供一个http/websocket反向代理

```
url_1, err := url.Parse("http://localhost:8081")
url_2, err := url.Parse("http://localhost:8082")
targets := []*middleware.ProxyTarget{
  {
    URL: url_1,
  },
  {
    URL: url_2,
  },
}

e.Use(middleware.ProxyWithConfig(middleware.ProxyConfig{
  Skipper: nil,
  Balancer: middleware.RoundRobinBalancer(targets),
}))
```

**Recover Middleware**

> 恢复中间件可以从任何地方的panic恢复, 打印栈追踪信息并把控制器权交给中心化的HTTPErrorHandler.

`e.Use(middleware.Recover())`
或
```
e.Use(middleware.RecoverWithConfig(middleware.RecoverConfig{
  Skipper: nil,
  StackSize:  4 << 10, // 10 KB
  DisableStackAll: false,
  DisablePrintStack: false,
}))
```

**Redirect Middleware**

> 重定向中间件, http请求重定向

```go
e.Pre(middleware.HTTPSRedirect())  //重定向到https://
e.Pre(middleware.HTTPSWWWRedirect())  //重定向到https://wwww.xx.com
e.Pre(middleware.HTTPSNonWWWRedirect())  //重定向到https://xx.com
e.Pre(middleware.WWWRedirect()) //重定向到http://www.xx.com
e.Pre(middleware.NonWWWRedirect()) //重定向到http://xx.com

e.Use(middleware.HTTPSRedirectWithConfig(middleware.RedirectConfig{
  Skipper: nil,
  Code: http.StatusTemporaryRedirect,
}))
```

**Static Middleware**

> 静态资源中间件, 处理静态资源查找

`e.Use(middleware.Static("/static"))`
或
```
e.Use(middleware.StaticWithConfig(middleware.StaticConfig{
  Skipper: nil,
  Root:   "static",
  Index: "index.html",
  HTML5: true,
  Browse: false,
}))
```

**Request ID Middleware**

> 为每个请求生成一个唯一的id

`e.Use(middleware.RequestID())`
或
```
e.Use(middleware.RequestIDWithConfig(middleware.RequestIDConfig{
  Skipper: nil,
  Generator: func() string {
    return customGenerator()
  },
}))
```
