all: deps build

.PHONY: deps
deps:
	go get -u github.com/dustin/go-broadcast/...
	go get -u github.com/manucorporat/stats/...
	go get -u github.com/gin-gonic/gin/...

.PHONY: build
build: deps
	go build -o chat .
