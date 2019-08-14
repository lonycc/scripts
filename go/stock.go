package main

import (
	"bufio"
	"flag"
	"fmt"
	"github.com/axgle/mahonia"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"strconv"
	"strings"
)

type SinaStock struct {
	Name     string
	Price    float64
	Percent  float64
	TickSize string
}

const Version = "0.0.1"

var format = flag.String("f", "term", "formatt output, term or vim")
var code = flag.String("c", "", "stock code")
var version = flag.Bool("v", false, "version number")
var help = flag.Bool("h", false, "display help info")
var stock_file = flag.String("r", "stock.list", "file with stock code")
var help_info = `Usage: stock [options]
Options:
  -v    output the version number
  -h    output usage information
  -f    display format, vim or term, (default term)
  -c    stock code, multi seprate with comma, sh000001,sh000002 etc
  -r    stock file, if -c set, -r will be ignored, (default stock.list)`
var (
	sname string
	err   error
)

func main() {
	flag.Parse()

	if *version {
		fmt.Printf("tiny stock tool %s\n", Version)
		return
	}

	if *help {
		fmt.Println(help_info)
		return
	}

	if *code == "" {
		sname, err = getStockList(path.Join(GetCurPath(), *stock_file))
		if err != nil {
			fmt.Println(err.Error())
			return //os.Exit(1)
		}
	} else {
		sname = *code
	}

	rList, err := GetSinaStock(sname)
	if err != nil {
		log.Fatal(err)
	}

	res := ""
	if *format == "term" {
		for _, item := range rList {
			res = formatForTerminal(item.Name, item.Price, item.Percent, item.TickSize)
			fmt.Println(res)
		}
	} else {
		item := rList[0]
		res = formatForVim(item.Price, item.Percent, item.TickSize)
		fmt.Println(res)
	}
}

func getStockList(filename string) (r string, err error) {
	f, err := os.Open(filename)
	if err != nil {
		return
	}
	defer f.Close()
	buf := bufio.NewReader(f)
	lines := make([]string, 0)
	for {
		line, err := buf.ReadString('\n')
		if err != nil {
			if err == io.EOF {
				if strings.TrimSpace(line) != "" {
					lines = append(lines, strings.TrimSpace(line))
				}
				break
			}
			return "", err
		}
		lines = append(lines, strings.TrimSpace(line))
	}
	r = strings.Join(lines, ",")
	return
}

func GetSinaStock(sname string) (list []*SinaStock, err error) {
	urlAdress := fmt.Sprintf("http://hq.sinajs.cn/list=%s", sname)
	req, err := http.Get(urlAdress)
	if err != nil {
		return
	}
	defer req.Body.Close()
	b, err := ioutil.ReadAll(req.Body)
	if err != nil {
		return
	}
	enc := mahonia.NewDecoder("gbk")
	content := enc.ConvertString(string(b))
	list = make([]*SinaStock, 0)
	for _, item := range strings.Split(content, ";") {
		if strings.TrimSpace(item) == "" {
			continue
		}
		index := strings.Index(item, "\"")
		rs := strings.Split(item[index+1:len(item)-1], ",")

		sinaStock := &SinaStock{
			Name:     "-",
			TickSize: "-",
		}

		if rs[0] != "" {
			sinaStock.Name = rs[0]
			price, _ := strconv.ParseFloat(rs[3], 10)
			old_price, _ := strconv.ParseFloat(rs[2], 10)
			sinaStock.Price = price
			zdfv := sinaStock.Price - old_price
			sinaStock.Percent = zdfv
			zdf := zdfv / old_price * 100
			sinaStock.TickSize = fmt.Sprintf("(%.2f%%)", zdf)
		}

		list = append(list, sinaStock)
	}
	return
}

func GetCurPath() string {
	file, _ := exec.LookPath(os.Args[0])
	path, _ := filepath.Abs(file)
	rst := filepath.Dir(path)
	return rst
}

func formatForTerminal(name string, price float64, delta float64, percentage string) string {
	var deltaFormatted string
	var percentageFormatted = percentage

	if delta > 0 {
		deltaFormatted = fmt.Sprintf("\x1b[31m+%.2f\x1b[0m", delta)
		percentageFormatted = fmt.Sprintf("\x1b[31m%s\x1b[0m", percentage)
	} else if delta < 0 {
		deltaFormatted = fmt.Sprintf("\x1b[32m%.2f\x1b[0m", delta)
		percentageFormatted = fmt.Sprintf("\x1b[32m%s\x1b[0m", percentage)
	} else {
		deltaFormatted = fmt.Sprintf("%.2f", delta)
	}
	return fmt.Sprintf("\x1b[32m%s\x1b[0m %.2f %s %s", name, price, deltaFormatted, percentageFormatted)
}

func formatForVim(price float64, delta float64, percentage string) string {
	var result string
	if delta > 0 {
		result = fmt.Sprintf(`echohl Normal
echo "%.2f"
echohl MoreMsg
echon " +%.2f %s"
echohl Normal`, price, delta, percentage)

	} else if delta < 0 {
		result = fmt.Sprintf(`echohl Normal
echo "%.2f"
echohl WarningMsg
echon " %.2f %s"
echohl Normal`, price, delta, percentage)
	} else {
		result = fmt.Sprintf(`echohl Normal
echo "%.2f"
echon " %.2f %s"
echohl Normal`, price, delta, percentage)
	}
	return result
}
