package main

import (
	"fmt"
	"strconv"
)

var s string = "CCCCOLLLCCCCCMOCCCCC"

func main() {
	var ptr int
	var output string
	var temp string
	var count int

	for i, v := range s {
		if byte(v) != s[ptr] {
			ptr = i
			output += temp
			count = 1
			temp = strconv.Itoa(count) + string(v)
		} else {
			count++
			temp = strconv.Itoa(count) + string(v)
			continue
		}
	}
	output += temp
	fmt.Println(output)
}
