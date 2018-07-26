package main


import (
	"C"
	"fmt"
)

//export printHelloWorld
func printHelloWorld() {
	fmt.Println("Hello from golang!")
}

func main() {}
