
hello-dyn: libhello.dylib main.c
	gcc -L. -lhello -o hello-dyn main.c

hello-static: libhello.a main.c
	gcc -static -L/usr/lib -L. -lhello -o hello-static main.c

libhello.dylib: hello.h hello.c
	gcc -dynamiclib -o libhello.dylib hello.c

libhello.a: hello.o
	ar rcs libhello.a hello.o

hello.o: hello.h hello.c
	gcc -static -c hello.c -o hello.o