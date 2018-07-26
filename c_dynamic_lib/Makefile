
.PHONY: clean

hello: libhello.dylib main.c
	gcc -L. -lhello -o $@ main.c

libhello.dylib: hello.h hello.c
	gcc -dynamiclib -o $@ hello.c

clean:
	-rm hello libhello.dylib libhello.a hello.o