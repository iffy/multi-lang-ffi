proc printHelloWorld() {.exportc, dynlib.} =
  echo "Hello from Nim!"
