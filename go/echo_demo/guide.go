package main

import (
	"encoding/json"
	"fmt"
	"html/template"
	"io"
	"net"
	"net/http"
	"time"

	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
	"github.com/labstack/gommon/log"
)

// 自定义http上下文
type CustomContext struct {
	echo.Context
}

func (c *CustomContext) Foo() {
	println("foo")
}

func (c *CustomContext) Bar() {
	println("bar")
}

// 模板渲染器
type TemplateRenderer struct {
	templates *template.Template
}

func (t *TemplateRenderer) Render(w io.Writer, name string, data interface{}, c echo.Context) error {
	if viewContext, isMap := data.(map[string]interface{}); isMap {
		viewContext["reverse"] = c.Echo().Reverse
	}

	return t.templates.ExecuteTemplate(w, name, data)
}

// 写入cookie
func writeCookie(c echo.Context) error {
	cookie := new(http.Cookie)
	cookie.Name = "username"
	cookie.Value = "tony"
	cookie.Expires = time.Now().Add(24 * time.Hour)
	cookie.HttpOnly = true
	cookie.Secure = false
	c.SetCookie(cookie)
	return c.String(http.StatusOK, "write a cookie")
}

// 读取cookie
func readCookie(c echo.Context) error {
	cookie, err := c.Cookie("username")
	if err != nil {
		return err
	}
	fmt.Println(cookie.Name)
	fmt.Println(cookie.Value)
	return c.String(http.StatusOK, "read a cookie")
}

// 遍历读取cookie
func readAllCookies(c echo.Context) error {
	for _, cookie := range c.Cookies() {
		fmt.Println(cookie.Name)
		fmt.Println(cookie.Value)
	}
	return c.String(http.StatusOK, "read all cookie")
}

// 自定义http错误处理
func customHTTPErrorHandler(err error, c echo.Context) {
	code := http.StatusInternalServerError
	if he, ok := err.(*echo.HTTPError); ok {
		code = he.Code
	}
	errorPage := fmt.Sprintf("%d.html", code)
	if err := c.File(errorPage); err != nil {
		c.Logger().Error(err)
	}
	c.Logger().Error(err)
}

// 单个文件上传
func upload(c echo.Context) error {
	file, err := c.FormFile("file")
	if err != nil {
		return err
	}
	src, err := file.Open()
	if err != nil {
		return err
	}
	defer src.Close()
	dst, err := os.Create(file.Filename)
	if err != nil {
		return err
	}
	defer dst.Close()
	if _, err = io.Copy(dst, src); err != nil {
		return err
	}
	return c.HTML(http.StatusOK, fmt.Sprintf("<p>File %s uploaded</p>", file.Filename))
}

// 多个文件上传
func multi_upload(c echo.Context) error {
	form, err := c.MultipartForm()
	if err != nil {
		return err
	}
	files := form.File["files"]
	for _, file := range files {
		src, err := file.Open()
		if err != nil {
			return err
		}
		defer src.Close()
		dst, err := os.Create(file.Filename)
		if err != nil {
			return err
		}
		defer dst.Close()
		if _, err = io.Copy(dst, src); err != nil {
			return err
		}
	}
	return c.HTML(http.StatusOK, fmt.Sprintf("<p>Uploaded successfully %d files", len(files)))
}

// 自定义数据绑定
type CustomBinder struct{}

func (cb *CustomBinder) Bind(i interface{}, c echo.Context) (err error) {
	// You may use default binder
	db := new(echo.DefaultBinder)
	if err = db.Bind(i, c); err != echo.ErrUnsupportedMediaType {
		return
	}
	// Define your custom implementation
	return
}

type User struct {
	Name  string `json:"name" xml:"name"`
	Email string `json:"email" xml:"email"`
}

func main() {
	// echo 示例
	e := echo.New()
	e.Logger.SetLevel(log.DEBUG)
	e.HideBanner = false
	e.HidePort = false
	e.Debug = true
	e.DisableHTTP2 = false
	e.Server.ReadTimeout = time.Second * 30
	e.Server.WriteTimeout = time.Minute * 1
	e.HTTPErrorHandler = customHTTPErrorHandler
	e.Static("/static", "assets") //请求/static/aa.js, 从assets/aa.js获取
	e.File("/favicon.ico", "images/favicon.ico") //请求指定文件

	// 闭包模式的中间件
	e.Use(func(h echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			cc := &CustomContext{c}
			return h(cc)
			//return echo.NewHTTPError(http.StatusUnauthorized, "Please provide valid credentials")
			//return echo.NewHTTPError(403)
		}
	})

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Route => handler
	e.GET("/", func(c echo.Context) error {
		u := &User{
			Name:  "Jon",
			Email: "jon@labstack.com",
		}
		//return c.String(http.StatusOK, "response as string")
		//return c.HTML(200, "<h1>response as html</h1>")
		// 当json串很大时, JSON()内部用json.Marsha1处理效率不高, 应当用stream json
		//return c.JSON(http.StatusOK, u)  //如果请求带?pretty则会美化输出
		//return c.JSONPretty(200, u, "	")
		//return c.File("/path/to/file")
		//return c.Attachment("/path/to/file", "title of file")
		//return c.Redirect(http.StatusMovedPermanently, "url")

		c.Response().Header().Set(echo.HeaderContentType, echo.MIMEApplicationJSONCharsetUTF8)
		c.Response().WriteHeader(200)
		return json.NewEncoder(c.Response()).Encode(u)
	})

  	// 使用自定义的上下文处理请求返回响应
	e.GET("/context", func(c echo.Context) error {
		cc := c.(*CustomContext)
		cc.Foo()
		cc.Bar()
		return cc.String(200, "OK")
	})

	e.GET("/test", func(c echo.Context) error {
		name := c.FormValue("name") //表单提交的数据
		// c.QueryParam("name")  //url?name=xxx
		return c.String(200, name)
	})

	renderer := &TemplateRenderer{
		templates: template.Must(template.ParseGlob("*.html")),
	}
	e.Renderer = renderer

	// 命名路由"foobar"
	e.GET("/something", func(c echo.Context) error {
		return c.Render(http.StatusOK, "template.html", map[string]interface{}{
			"name": "Dolly!",
		})
	}).Name = "foobar"
	
	// 指定静态目录在根目录public路径下
	e.STATIC("/", "public")
	e.POST("/upload", upload)

	// e.Any(path string, h Handler)  //任何方法
	// e.Match(methods []string, path string, h Handler)

	// g := e.Group("/admin")
	// g.Use(m ...Middleware)

	// 命名路由
	// n := e.Post(path string, h Handler)
	// n.Name = "n-post-xx"
	// or
	// e.DELETE(path string, h Handler).Name = "delete-xx"

	// uri构造
	// e.URI(handler HandlerFunc, params ...interface{})
	// e.Reverse(name string, params ...interface{})  // 第一个参数时命名路由

	// 全部注册过的路由
	// data, err := json.MarshalIndent(e.Routes(), "", "  ")

	// Start server
	//e.Logger.Fatal(e.Start(":1323"))

	// or
	/*
		s := &http.Server{
			Addr:         ":1323",
			ReadTimeout:  20 * time.Minute,
			WriteTimeout: 20 * time.Minute,
		}
		e.Logger.Fatal(e.StartServer(s))
	*/

	// or
	l, err := net.Listen("tcp", ":1323")
	if err != nil {
		e.Logger.Fatal(l)
	}
	e.Listener = l
	e.Logger.Fatal(e.Start(""))
}
