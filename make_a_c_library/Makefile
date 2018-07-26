
hellobin: libhello.dylib main.c
	gcc -L. -lhello -o hellobin main.c

libhello.dylib: hello.h hello.c
	gcc -dynamiclib -o libhello.dylib hello.c
