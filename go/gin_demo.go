package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	gin.SetMode(gin.DebugMode)
	router := gin.Default()

	//添加中间件
	router.Use(Middleware)
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
	fmt.Println("this is a middle ware")
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
