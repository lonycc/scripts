GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
BINARY_NAME=chat
BINARY_LINUX=$(BINARY_NAME)_linux64
BINARY_WINDOWS=$(BINARY_NAME)_win64.exe

.PHONY: all
all: deps build

.PHONY: deps
deps:
	$(GOGET) -u github.com/dustin/go-broadcast/...
	$(GOGET) -u github.com/manucorporat/stats/...
	$(GOGET) -u github.com/gin-gonic/gin/...

.PHONY: build
build: deps
	$(GOBUILD) -o chat .

.PHONY: clean
clean:
	$(GOCLEAN)
	rm -f $(BINARY_NAME)
	rm -f $(BINARY_LINUX)
	rm -f $(BINARY_WINDOWS)

.PHONY: run
run:
	$(GOBUILD) -o $(BINARY_NAME) -v ./...
	./$(BINARY_NAME)

.PHONY: test
test:
	$(GOTEST) -v ./...

build-linux:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 $(GOBUILD) -o $(BINARY_LINUX) -v

build-windows:
	GOOS=windows GOARCH=amd64 $(GOBUILD) -o $(BINARY_WINDOWS) -v
