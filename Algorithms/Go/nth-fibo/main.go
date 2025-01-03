package main

import "fmt"

func main() {
	fmt.Println(nthFibo(5))
}

func nthFibo(n int) int {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		x, y = y, x+y
	}
	return x
}
