#!/usr/bin/env node

const ffi = require('ffi');

function trylib(path) {
  try {
    console.log(path);
    const lib = ffi.Library(path, {
      'printHelloWorld': ['void', []]
    });
    lib.printHelloWorld();
  } catch(err) {
    console.log(err)
  }
}

trylib("../c_dynamic_lib/libhello")
trylib("../c_shared_lib/libhello")
trylib("../go_shared_lib/libecho")
