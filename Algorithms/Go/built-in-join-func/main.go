package main

import "fmt"

func main() {
	slice := []string{"apple", "banana", "mango", "amir!"}
	output := join(",", slice)
	fmt.Printf("normal join --> %v\n", output)

	output2 := variadicJoin(",", "beach", "mountain", "jungle")
	fmt.Printf("variadic join --> %v\n", output2)
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

func variadicJoin(del string, values ...string) string {
	var line string
	for i, ele := range values {
		line = line + ele
		if i != len(values)-1 {
			line += del + " "
		}
	}
	return line
}
