package main

import (
	"fmt"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/contrib/sessions"
	"github.com/gin-gonic/gin"
	"net/http"
)

type JsonHolder struct {
	Id   int    `json:"id"`
	Name string `json:"name"`
}

func main() {
	gin.SetMode(gin.DebugMode)

	router := gin.Default()

	//添加中间件
	store, _ := sessions.NewRedisStore(10, "tcp", "localhost:6379", "", []byte("secret"))
	router.Use(sessions.Sessions("test-session", store))
	store.Options(sessions.Options{
		MaxAge:   3600,
		Path:     "/",
		Secure:   true,
		HttpOnly: true,
	})

	router.Use(Middleware)
	router.Use(cors.New(cors.Config{
		AllowOrigins:  []string{"*"},
		AllowMethods:  []string{"PUT", "PATCH", "GET", "POST", "DELETE"},
		AllowHeaders:  []string{"content-type"},
		ExposeHeaders: []string{"X-Total-Count"},
	}))
	//注册接口
	router.GET("/get", GetHandler)
	router.GET("/test", TestHandler)
	router.POST("/post", PostHandler)
	router.PUT("/put", PutHandler)
	router.DELETE("/delete", DeleteHandler)
	//监听端口
	//http.ListenAndServe(":8080", router)
	router.Run(":8080")
}

func Middleware(c *gin.Context) {
	fmt.Println("this is a middleware")
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
	holder := JsonHolder{Id: 1, Name: "my name"}
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
