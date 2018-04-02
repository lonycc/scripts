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
