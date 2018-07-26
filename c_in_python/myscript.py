from ctypes import cdll

lib = cdll.LoadLibrary("../libhello.a")
lib.printHelloWorld()
