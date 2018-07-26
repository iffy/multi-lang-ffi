#!/usr/bin/env python
from ctypes import cdll

def trylib(path):
    try:
        print path
        lib = cdll.LoadLibrary(path)
        lib.printHelloWorld()
    except Exception as e:
        print(e)

trylib("../c_dynamic_lib/libhello.dylib")
trylib("../c_shared_lib/libhello.so")
trylib("../go_shared_lib/libecho.so")
trylib("../rust_shared_lib/target/release/libhello.dylib")
trylib("../nim_shared_lib/libhello.dylib")
