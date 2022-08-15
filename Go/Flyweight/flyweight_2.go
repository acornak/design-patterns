package main

import (
	"fmt"
	"strings"
)

type User struct {
	FullName string
}

func NewUser(fullname string) *User {
	return &User{fullname}
}

var allNames []string

type User2 struct {
	names []uint8
}

func NewUser2(fullname string) *User2 {
	getOrAdd := func(s string) uint8 {
		for i := range allNames {
			if allNames[i] == s {
				return uint8(i)
			}
		}
		allNames = append(allNames, s)
		return uint8(len(allNames) - 1)
	}
	result := User2{}
	parts := strings.Split(fullname, " ")
	for _, p := range parts {
		result.names = append(result.names, getOrAdd(p))
	}
	return &result
}

func (u *User2) FullName() string {
	var parts []string
	for _, id := range u.names {
		parts = append(parts, allNames[id])
	}
	return strings.Join(parts, " ")
}

func main() {
	john := NewUser("John Doe")
	alsoJohn := NewUser("John Smith")
	jane := NewUser("Jane Doe")
	alsoJane := NewUser("Jane Smith")
	memory := len([]byte(john.FullName)) + len([]byte(alsoJohn.FullName)) + len([]byte(jane.FullName)) + len([]byte(alsoJane.FullName))

	fmt.Println("Memory taken by users: ", memory)

	john2 := NewUser2("John Doe")
	alsoJohn2 := NewUser2("John Smith")
	jane2 := NewUser2("Jane Doe")
	alsoJane2 := NewUser2("Jane Smith")
	memory2 := 0
	for _, a := range allNames {
		memory2 += len([]byte(a))
	}

	memory2 += len(john2.names)
	memory2 += len(alsoJohn2.names)
	memory2 += len(jane2.names)
	memory2 += len(alsoJane2.names)

	fmt.Println("Memory taken by users2: ", memory2)
}
