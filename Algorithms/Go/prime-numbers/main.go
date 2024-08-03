// prime numbers between 2 to N
package main

import "fmt"

func primeTo(N int) (primes []int) {
	b := make([]bool, N)
	for i := 2; i < N; i++ {
		if b[i] {
			continue
		}
		primes = append(primes, i)
		for k := i * i; k < N; k += i {
			b[k] = true
		}
	}
	return
}

func main() {
	primes := primeTo(100)
	for _, p := range primes {
		fmt.Printf("%d\n", p)
	}
}
