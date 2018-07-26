
.PHONY: clean

# dynamically linked

hello-dyn: libhello.dylib main.c
	gcc -L. -lhello -o $@ main.c

libhello.dylib: hello.h hello.c
	gcc -dynamiclib -o $@ hello.c

# statically linked

hello-static: libhello.a main.c
	gcc -L. -lhello -o $@ main.c

libhello.a: hello.o
	libtool -static -o $@ hello.o

hello.o: hello.h hello.c
	gcc -static -c hello.c -o $@




clean:
	-rm hello-dyn hello-static libhello.dylib libhello.a hello.o