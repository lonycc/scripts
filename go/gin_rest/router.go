package main

import (
	. "./apis"
	"fmt"
	"github.com/gin-gonic/gin"
)

func main() {
	gin.SetMode(gin.DebugMode)
	router := gin.Default()

	// 使用中间件, 每次路由请求都会调用
	router.Use(Middleware)
	router.Use(gin.Logger())
	router.Use(gin.Recovery())

	v1 := router.Group("/api/v1/person")
	// 只对该分组应用中间件
	// v1.Use(xxMiddleware.MiddlewareFunc())
	{
		v1.POST("/", AddPerson)
		v1.GET("/", GetPersons)
		v1.GET("/:id", GetPerson)
		v1.PUT("/:id", UpdatePerson)
		v1.DELETE("/:id", DestroyPerson)
	}
	router.Run(":8080")
}

func Middleware(c *gin.Context) {
	fmt.Println("this is a middle ware")
}
