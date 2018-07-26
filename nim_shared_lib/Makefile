.PHONY: all

all: libhello.dylib libhello.a

libhello.dylib: hello.nim
	nim c --app:lib -d:release hello.nim

libhello.a: hello.nim
	nim c --app:staticlib -d:release hello.nim
