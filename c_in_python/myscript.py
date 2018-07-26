from ctypes import cdll

try:
    lib = cdll.LoadLibrary("../c_dynamic_lib/libhello.dylib")
    print 'dynamic'
    lib.printHelloWorld()
except Exception as e:
    print(e)

try:
    lib = cdll.LoadLibrary("../c_shared_lib/libhello.so")
    print 'shared'
    lib.printHelloWorld()
except Exception as e:
    print(e)
