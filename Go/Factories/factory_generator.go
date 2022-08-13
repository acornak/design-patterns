package main

import "fmt"

type Employee struct {
	Name, Position string
	AnnualIncome   int
}

// functional approach
func NewEmployeeFactory(position string, annualIncome int) func(name string) *Employee {
	return func(name string) *Employee {
		return &Employee{name, position, annualIncome}
	}
}

// structural approach
type EmployeeFactory struct {
	position     string
	annualIncome int
}

func (ef *EmployeeFactory) Create(name string) *Employee {
	return &Employee{name, ef.position, ef.annualIncome}
}

func NewEmployeeFactory2(position string, annualIncome int) *EmployeeFactory {
	return &EmployeeFactory{position, annualIncome}
}

func main() {
	// functional approach
	developerFactory := NewEmployeeFactory("developer", 60000)
	managerFactory := NewEmployeeFactory("manager", 80000)

	developer := developerFactory("Adam")
	manager := managerFactory("Jane")

	fmt.Println(developer)
	fmt.Println(manager)

	// structural approach
	bossFactory := NewEmployeeFactory2("CEO", 120000)
	bossFactory.annualIncome = 135000
	boss := bossFactory.Create("Anton")

	fmt.Println(boss)
}
