package main

import "fmt"

type Person struct {
	Name     string
	Age      int
	EyeCount int
}

// default value
func NewPerson(name string, age int) *Person {
	if age < 16 {
		// ...
	}

	return &Person{name, age, 2}
}

func main() {
	p := NewPerson("John", 30)
	p.EyeCount = 1
	fmt.Println(p)
}
