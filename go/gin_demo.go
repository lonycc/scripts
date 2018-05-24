package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/gin-gonic/contrib/sessions"
	"net/http"
)

func main() {
	gin.SetMode(gin.DebugMode)
	router := gin.Default()

	//添加中间件
	store, _ := sessions.NewRedisStore(10, "tcp", "localhost:6379", "", []byte("secret"))
	router.Use(sessions.Sessions("test-session", store))
	store.Options(sessions.Options{
		MaxAge: 3600,
		Path: "/",
		Secure: true,
		HttpOnly: true,
	})
	
	router.Use(Middleware)
	router.Use(CORSMiddleware)
	//注册接口
	router.GET("/get", GetHandler)
	router.POST("/post", PostHandler)
	router.PUT("/put", PutHandler)
	router.DELETE("/delete", DeleteHandler)
	//监听端口
	http.ListenAndServe(":8080", router)
	//router.Run(":8080")
}

func Middleware(c *gin.Context) {
	fmt.Println("this is a middleware")
}

// 跨域允许中间件
func CORSMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "http://localhost")
		c.Writer.Header().Set("Access-Control-Max-Age", "86400")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE, UPDATE")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Origin, Authorization, Accept, Client-Security-Token, Accept-Encoding, x-access-token")
		c.Writer.Header().Set("Access-Control-Expose-Headers", "Content-Length")
		c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")

		if c.Request.Method == "OPTIONS" {
			fmt.Println("OPTIONS")
			c.AbortWithStatus(200)
		} else {
			c.Next()
		}
	}
}

func GetHandler(c *gin.Context) {
	value, exist := c.GetQuery("key")
	if !exist {
		value = "this key is not exist"
	}
	c.Data(http.StatusOK, "text/plain", []byte(fmt.Sprintf("get success! %s\n", value)))
	return
}

func PostHandler(c *gin.Context) {
	type JsonHolder struct {
		Id   int    `json:"id"`
		Name string `json:"name"`
	}
	holder := JsonHolder{Id: 1, Name: "my name"}
	//若返回json数据，可以直接使用gin封装好的JSON方法
	c.JSON(http.StatusOK, holder)
	return
}

func PutHandler(c *gin.Context) {
	c.Data(http.StatusOK, "text/plain", []byte("put success!\n"))
	return
}

func DeleteHandler(c *gin.Context) {
	c.Data(http.StatusOK, "text/plain", []byte("delete success!\n"))
	return
}

// 测试redis存取
func TestHandler(c *gin.Context) {
	session := sessions.Default(c)
	v := session.Get("count")
	var count int
	if v == nil {
		count = 0
	} else {
		count = v.(int)
		count += 1
	}
	session.Set("count", 0)
	session.Save()
	c.JSON(200, gin.H{"count": count})
}
