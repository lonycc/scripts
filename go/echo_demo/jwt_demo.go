package main

import (
	"net/http"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
)

type jwtCustomClaims struct {
	Name  string `json:"name"`
	Admin bool   `json:"admin"`
	jwt.StandardClaims
}

type User struct {
	Username string `json: "username"`
	Password string `json: "password"`
}

func login(c echo.Context) error {
	//username := c.FormValue("username")
	//password := c.FormValue("password")
	
	u := new(User)
	if err := c.Bind(u); err != nil {
		return err
	}
	username := u.Username
	password := u.Password
	
	if username == "aaa" && password == "bbb" {
		// Create token
		token := jwt.New(jwt.SigningMethodHS256)

		// Set claims
		claims := token.Claims.(jwt.MapClaims)
		claims["name"] = username
		claims["admin"] = true
		claims["exp"] = time.Now().Add(time.Hour * 1).Unix()

		// Generate encoded token and send it as response.
		t, err := token.SignedString([]byte("secret"))
		if err != nil {
			return err
		}
		return c.JSON(http.StatusOK, map[string]string{
			"token": t,
			"code":  "200",
		})
	}
	return echo.ErrUnauthorized
}

func accessible(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]string{
		"code":    "200",
		"message": "this is public",
	})
}

func restricted(c echo.Context) error {
	user := c.Get("user").(*jwt.Token)
	claims := user.Claims.(jwt.MapClaims)
	// name := claims["name"].(string)
	// admin := claims["admin"](.bool)
	return c.JSON(http.StatusOK, claims)
}

func main() {
	e := echo.New()

	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Login route
	e.POST("/login", login)

	// Unauthenticated route
	e.GET("/", accessible)

	// Restricted group
	r := e.Group("/restricted")
	r.Use(middleware.JWT([]byte("secret")))
	r.GET("", restricted)

	e.Logger.Fatal(e.Start(":1323"))
}

/*
form 表单方式提交
curl -X POST -d 'username=aaa&password=bbb' localhost:1323/login
json格式提交
curl -X POST -H 'Content-Type: application/json' -d '{"username": "aaa", "password": "bbb"}' localhost:1323/login

curl localhost:1323/restricted -H "Authorization: Bearer xxxx"
curl -X GET localhost:1323/
*/
