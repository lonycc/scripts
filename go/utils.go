package main

import (
	"fmt"
	"github.com/fatih/color"
	"github.com/joho/godotenv"
	"golang.org/x/net/proxy"
	"log"
	"net/http"
	"os"
	"io/ioutil"
	"path/filepath"
	"regexp"
	"runtime"
	"strings"
	"unicode"
)

func SysInfo() {
	fmt.Printf("os %s", runtime.GOOS)
	fmt.Printf("arch %s", runtime.GOARCH)
	fmt.Printf("compiler %s", runtime.Compiler)
}

func GetExecutePath() string {
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	return filepath.Dir(ex)
}

func IsChinese(str string) bool {
	for _, r := range str {
		if unicode.Is(unicode.Scripts["Han"], r) {
			return true
		}
	}
	return false
}

func LoadEnv(file string) {
	if _, err := os.Stat(file); os.IsNotExist(err) {
		return
	}
	err := godotenv.Load(file)
	if err != nil {
		log.Fatal("Error loading .env file")
		return
	}
	//os.Getenv("key")
}

func HttpClient(proxy_c string, url string) {
	client := &http.Client{}
	dialer, err := proxy.SOCKS5("tcp", proxy_c, nil, proxy.Direct)
	if err != nil {
		color.Red("Can not connect to the proxy: %s", proxy_c)
		os.Exit(1)
	}

	httpTransport := &http.Transport{}
	client.Transport = httpTransport
	httpTransport.Dial = dialer.Dial
	resp, err := client.Get(url)
	defer resp.Body.Close()
	if err != nil {
		color.Red("Query failed with err: %s", err.Error())
		os.Exit(1)
	}
	html, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		color.Red("ioutil.ReadAll with error: %s", err.Error())
		os.Exit(1)
	}
	color.Green(resp.html)
}

func LoopBit() {
	c := make(chan int)
	go func() {
		for {
			fmt.Print(<-c, " ")
		}
	}()
	for {
		select {
		case c <- 0:
		case c <- 1:
		}
	}
}

// 标准库遍历
func FileList1(path string) {
	filepath.Walk(path, func (path string, info os.FileInfo, err error) error {
		s, _ := os.Stat(path)
		if s.IsDir() {
        	fmt.Println(path)
        } else {
        	fmt.Println("-------")
        }
        return nil
    })
}

// 递归遍历目录
func FileList2(path string) {
    fs, _ := ioutil.ReadDir(path)
    for _, file := range fs {
    	new_path := path + "/" + file.Name()
    	fmt.Println(new_path)
        if file.IsDir() {
            FileList2(new_path)
        }
    }
}
