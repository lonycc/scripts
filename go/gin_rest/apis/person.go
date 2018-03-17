package apis

import (
	. "../models"
	"fmt"
	"github.com/gin-gonic/gin"
	//"log"
	"net/http"
	"strconv"
	"strings"
)

func AddPerson(c *gin.Context) {
	first_name := c.Request.FormValue("first_name")
	last_name := c.Request.FormValue("last_name")

	if strings.TrimSpace(first_name) == "" || strings.TrimSpace(last_name) == "" {
		c.JSON(http.StatusOK, gin.H{
			"msg": "first_name和last_name不能为空",
		})
		return
	}

	p := Person{FirstName: first_name, LastName: last_name}

	rs, err := p.AddPerson()
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": "新建用户失败",
		})
		return
	}
	msg := fmt.Sprintf("新建用户成功, 其id为%d", rs)
	c.JSON(http.StatusOK, gin.H{
		"msg": msg,
	})
	return
}

func GetPersons(c *gin.Context) {
	p := Person{}
	persons, err := p.GetPersons()
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": "没有用户",
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"persons": persons,
	})
	return
}

func GetPerson(c *gin.Context) {
	cid := c.Param("id")
	id, err := strconv.Atoi(cid)
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": cid + "不是有效的数字",
		})
		return
	}
	p := Person{Id: id}
	msg, err := p.GetPerson()
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": "id为" + cid + "的用户不存在",
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"data": msg,
	})
	return
}

func DestroyPerson(c *gin.Context) {
	cid := c.Param("id")
	id, err := strconv.Atoi(cid)
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": cid + "不是有效的数字",
		})
		return
	}

	p := Person{Id: id}
	rs, err := p.DelPerson()
	if err != nil || rs == 0 {
		c.JSON(http.StatusOK, gin.H{
			"msg": "id为" + cid + "的用户不存在",
		})
		return
	}
	msg := fmt.Sprintf("Delete person %d", rs)
	c.JSON(http.StatusOK, gin.H{
		"msg": msg,
	})
	return
}

func UpdatePerson(c *gin.Context) {
	cid := c.Param("id")
	id, err := strconv.Atoi(cid)
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": cid + "不是有效的数字",
		})
		return
	}

	first_name := c.Request.FormValue("first_name")
	last_name := c.Request.FormValue("last_name")
	if strings.TrimSpace(first_name) == "" || strings.TrimSpace(last_name) == "" {
		c.JSON(http.StatusOK, gin.H{
			"msg": "first_name和last_name不能为空",
		})
		return
	}

	p := Person{Id: id, FirstName: first_name, LastName: last_name}
	rs, err := p.UpdatePerson()
	if err != nil || rs == 0 {
		c.JSON(http.StatusOK, gin.H{
			"msg": "更新失败",
		})
		return
		// log.Fatalln(err)
	}
	msg := fmt.Sprintf("更新id为%d的用户成功", p.Id)
	c.JSON(http.StatusOK, gin.H{
		"msg": msg,
	})
	return
}
