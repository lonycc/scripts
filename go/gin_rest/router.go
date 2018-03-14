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

	v1 := router.Group("/api/v1/person")
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
