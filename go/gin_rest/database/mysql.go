package database

import (
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
	"log"
)

var SqlDB *sql.DB

func init() {
	var err error
	SqlDB, err = sql.Open("mysql", "root:123456@tcp(127.0.0.1:3306)/test?parseTime=true")
	// defer SqlDB.Close()
	if err != nil {
		log.Fatal(err.Error())
	}

	SqlDB.SetMaxIdleConns(20)
	SqlDB.SetMaxOpenConns(20)

	err = SqlDB.Ping()
	if err != nil {
		log.Fatal(err.Error())
	}
}
