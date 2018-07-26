
.PHONY: clean

hello: libhello.a main.c
	gcc -L. -lhello -o $@ main.c

libhello.a: hello.o
	libtool -static -o $@ hello.o

hello.o: hello.h hello.c
	gcc -static -c hello.c -o $@

clean:
	-rm hello libhello.a hello.o