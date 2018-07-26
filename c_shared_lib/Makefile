
.PHONY: clean

hello: libhello.so main.c
	gcc -L. -lhello -o $@ main.c

libhello.so: hello.o
	gcc -shared -o $@ hello.o

hello.o: hello.c hello.h
	gcc -c -Wall -Werror -fpic hello.c

clean:
	-rm hello libhello.so hello.o
