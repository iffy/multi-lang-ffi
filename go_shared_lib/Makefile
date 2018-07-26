all: libecho.so libecho.dylib


libecho.so: echo.go
	go build -o $@ -buildmode=c-shared echo.go

libecho.dylib: echo.go
	go build -o $@ -buildmode=c-shared echo.go