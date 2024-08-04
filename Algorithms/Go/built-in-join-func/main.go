package main

import "fmt"

func main() {
	slice := []string{"apple", "banana", "mango", "amir!"}
	output := join(",", slice)
	fmt.Println(output)
}

func join(del string, values []string) string {
	var line string
	for i, ele := range values {
		line = line + ele
		if i != len(values)-1 {
			line = line + del + " "
		}
	}
	return line
}
