**echo框架入门介绍和使用demo**

> echo框架相当轻量, 核心只提供了http请求处理、路由配置以及中间件使用.ORM、RPC之类都由第三方包提供, 有很大的灵活性.

## 中间件

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

**Key Auth Middleware**

> 基于key的认证中间件

```
e.Use(middleware.KeyAuth(func(key string, c echo.Context) (bool, error) {
  return key == "valid-key", nil
}))

// 或
e.Use(middleware.KeyAuthWithConfig(middleware.KeyAuthConfig{
  Skipper: nil,
  // 也可选header:Authorization
  KeyLookup: "query:api-key",
  AuthScheme: "Bearer",
  Validator: func() bool {},
}))
```

**Gzip Middleware**

> 压缩http响应

```
e.Use(middleware.GzipWithConfig(middleware.GzipConfig{
  Skipper: nil,
  Level: 5,
}))
```

**Secure Middleware**

> 该中间件提供xss防护.

`e.Use(middleware.Secure())`
或
```
e.Use(middleware.SecureWithConfig(middleware.SecureConfig{
	Skipper: nil,
	XSSProtection: "1; mode=block",
	ContentTypeNosniff: "nosniff",
	XFrameOptions: "SAMEORIGIN",
	HSTSMaxAge: 0,
	HSTSExcludeSubdomains: false,
	ContentSecurityPolicy: "default-src 'self'",
}))
```

**Rewrite Middleware**

> url重写中间件

```
e.Pre(middleware.Rewrite(map[string]string{
  "/old":              "/new",
  "/api/*":            "/$1",
  "/js/*":             "/public/javascripts/$1",
  "/users/*/orders/*": "/user/$1/order/$2",
}))

// 或
e.Pre(middleware.RewriteWithConfig(middleware.RewriteConfig{
	Skipper: nil,
	Rules: map[string]string{},
}))
```

**Trailing Slash Middleware**

> 尾斜杠中间件, 给URI末尾加斜杠.

```
e.Pre(middleware.AddTrailingSlash())
e.Pre(middleware.RemoveTrailingSlash())

e.Use(middleware.AddTrailingSlashWithConfig(middleware.TrailingSlashConfig{
  Skipper: DefaultSkipper,
  RedirectCode: http.StatusMovedPermanently,
}))
```

**Session Middleware**

> http 会话管理, 默认的实现提供cookie和文件系统两种会话存储方式;

```
e.Use(session.Middleware(sessions.NewCookieStore([]byte("secret"))))

// 或
e.Use(session.MiddlewareWithConfig(session.Config{
	Skipper: nil,
	Store: sessions.NewCookieStore([]byte("secret")),
}))

e.GET("/", func(c echo.Context) error {
  sess, _ := session.Get("session", c)
  sess.Options = &sessions.Options{
    Path:     "/",
    MaxAge:   86400 * 7,
    HttpOnly: true,
  }
  sess.Values["foo"] = "bar"
  sess.Save(c.Request(), c.Response())
  return c.NoContent(http.StatusOK)
})
```

## cookbook

**自动tls**

> 从Let's Encrypt获取tls证书并自动绑定到域名

```
import "golang.org/x/crypto/acme/autocert"

// 主机白名单, 需严格匹配
e.AutoTLSManager.HostPolicy = autocert.HostWhitelist("domain.com")
// 缓存证书
e.AutoTLSManager.Cache = autocert.DirCache("/path/to/.cache")
e.Logger.Fatal(e.StartAutoTLS(":443"))

// 指定证书和公钥
//e.Logger.Fatal(e.StartTLS(":1323", "cert.pem", "key.pem"))
```

**内嵌资源**

```
import "github.com/GeertJohan/go.rice"

assetHandler := http.FileServer(rice.MustFindBox("app").HTTPBox())
// 返回app/index.html
e.GET("/", echo.WrapHandler(assetHandler))
// 对静态资源自动加前缀/static/
e.GET("/static/*", echo.WrapHandler(http.StripPrefix("/static/", assetHandler)))
```

**响应形式**
```
e.GET("/html", func(c echo.Context) error {
	return c.HTML(200, `<p>this is html</p>`)
})
e.GET("/file", func(c echo.Context) error {
	return c.File("file.go")
})
e.GET("/inline", func(c echo.Context) error {
	return c.Inline("file.go", "displayed.go")
})
e.GET("/attachment", func(c echo.Context) error {
	return c.Attachment("file.go", "saved.go")
})
```

**子域名**
```
type (
	Host struct {
		Echo *echo.Echo
	}
)

hosts := map[string]*Host{}

api := echo.New()
hosts["api.localhost:1323"] = &Host{api}
api.GET("/", func(c echo.Context) (err error) {
	retrun c.JSON(http.StatusOK, "this is api"}
}

admin := echo.New()
hosts["admin.localhost:1323"] = &Host{admin}
admin.GET("/", func(c echo.Context) (err error) {
	return c.String(200, "this is admin")
}

e := echo.New()
e.Any("/*", func(c echo.Context) (err error) {
	req := c.Request()
	res := c.Response()
	host := hosts[req.Host]
	if host == nil {
		err = echo.ErrNotFound
	} else {
		host.Echo.ServeHTTP(res, req)
	}
	return
})
e.Logger.Fatal(e.Start(":1323"))
```

**http2 服务端推送**
```
func main() {
	e := echo.New()
	e.Static("/", "static")
	e.GET("/", func(c echo.Context) (err error) {
		pusher, ok := c.Response().Writer.(http.Pusher)
		if ok {
			if err = pusher.Push("/app.css", nil); err != nil {
				return
			}
			if err = pusher.Push("/app.js", nil); err != nil {
				return
			}
			if err = pusher.Push("/echo.png", nil); err != nil {
				return
			}
		}
		return c.File("index.html")
	})
	e.Logger.Fatal(e.StartTLS(":1323", "cert.pem", "key.pem")
)
```

**jsonp请求和响应**
```
// curl localhost:1323/jsonp?callback=?
var content struct {
	Response  string    `json:"response"`
	Timestamp time.Time `json:"timestamp"`
	Random    int       `json:"random"`
}

e.GET("/jsonp", func(c echo.Context) error {
	callback := c.QueryParam("callback")
	content.Response = "Sent via JSONP"
	content.Timestamp = time.Now().UTC()
	content.Random = rand.Intn(1000)
	return c.JSONP(http.StatusOK, callback, &content)
})
```
**jwt认证授权**
```
import "github.com/dgrijalva/jwt-go"

type jwtCustomClaims struct {
	Name  string `json:"name"`
	Admin bool   `json:"admin"`
	jwt.StandardClaims
}

func login(c echo.Context) error {
	username := c.FormValue("username")
	password := c.FormValue("password")

	if username == "aaa" && password == "bbb" {
	
		/* payload声明, 采用的映射声明
		token := jwt.New(jwt.SigningMethodHS256)
		
		claims := token.Claims.(jwt.MapClaims)
		claims["name"] = "tony"
		claims["admin"] = true
		claims["exp"] = time.Now().Add(time.Hour * 72).Unix()
		*/
		
		/* 自定义payload声明
		claims := &jwtCustomClaims{
			"tony",
			true,
			jwt.StandardClaims{
				ExpiresAt: time.Now().Add(time.Hour * 72).Unix(),
			},
		}
		token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
		*/

		
		t, err := token.SignedString([]byte("secret"))
		if err != nil {
			return err
		}
		return c.JSON(http.StatusOK, map[string]string{
			"token": t,
			"code": "200",
		})
	}
	return echo.ErrUnauthorized
}

func auth(c echo.Context) error {
	user := c.Get("user").(*jwt.Token)
	
	/* 自定义payload声明
	claims := user.Claims.(*jwtCustomClaims)
	name := claims.Name
	*/
	
	/* 映射声明
	claims := user.Claims.(jwt.MapClaims)
	name := claims["name"].(string)
	*/
	
	return c.JSON(http.StatusOK, claims)
}

func main() {
	e := echo.New()
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	e.POST("/login", login)
	
	r := e.Group("/auth")
	
	/* 自定义声明
	config := middleware.JWTConfig{
		Claims:     &jwtCustomClaims{},
		SigningKey: []byte("secret"),
	}
	r.Use(middleware.JWTWithConfig(config))
	*/
	
	/* 映射声明
	r.Use(middleware.JWT([]byte("secret")))
	*/
	
	r.GET("", auth)
	e.Logger.Fatal(e.Start(":1323"))
}
```

**流式响应**

```
var locations = []Geolocation{}
e.GET("/", func(c echo.Context) error {
	c.Response().Header().Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	c.Response().WriteHeader(http.StatusOK)
	for _, l := range locations {
		if err := json.NewEncoder(c.Response()).Encode(l); err != nil {
			return err
		}
		c.Response().Flush()
		time.Sleep(1 * time.Second)
	}
	return nil
})
```
