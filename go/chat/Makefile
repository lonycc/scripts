GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
BINARY_NAME=chat
BINARY_LINUX=$(BINARY_NAME)_linux64
BINARY_WINDOWS=$(BINARY_NAME)_win64.exe
BINARY_MACOS=$(BINARY_NAME)_macos_64

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
	rm -f $(BINARY_MACOS)

.PHONY: run
run:
	$(GOBUILD) -o $(BINARY_NAME) -v ./...
	./$(BINARY_NAME)

.PHONY: test
test:
	$(GOTEST) -v ./...

build-linux:
	CGO_ENABLED=1 GOOS=linux GOARCH=amd64 $(GOBUILD) -o $(BINARY_LINUX) -v

build-windows:
	CGO_ENABLED=1 GOOS=windows GOARCH=amd64 $(GOBUILD) -o $(BINARY_WINDOWS) -v

build-macos:
	GOOS=darwin GOARCH=amd64 $(GOBUILD) -o $(BINARY_MACOS) -v
