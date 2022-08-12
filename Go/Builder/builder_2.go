package main

import "fmt"

type Person struct {
	StreetAddress, Postcode, City string
	CompanyName, Position         string
	AnnualIncome                  int
}

type PersonBuilder struct {
	person *Person
}

func (b *PersonBuilder) Lives() *PersonAddressBuilder {
	return &PersonAddressBuilder{*b}
}

func (b *PersonBuilder) Works() *PersonJobBuilder {
	return &PersonJobBuilder{*b}
}

type PersonAddressBuilder struct {
	PersonBuilder
}

type PersonJobBuilder struct {
	PersonBuilder
}

func (pab *PersonAddressBuilder) At(streetAddress string) *PersonAddressBuilder {
	pab.person.StreetAddress = streetAddress
	return pab
}

func (pab *PersonAddressBuilder) In(city string) *PersonAddressBuilder {
	pab.person.City = city
	return pab
}

func (pab *PersonAddressBuilder) Postcode(postcode string) *PersonAddressBuilder {
	pab.person.Postcode = postcode
	return pab
}

func (pjb *PersonJobBuilder) At(companyName string) *PersonJobBuilder {
	pjb.person.CompanyName = companyName
	return pjb
}

func (pjb *PersonJobBuilder) AsA(position string) *PersonJobBuilder {
	pjb.person.Position = position
	return pjb
}

func (pjb *PersonJobBuilder) Earning(annualIncome int) *PersonJobBuilder {
	pjb.person.AnnualIncome = annualIncome
	return pjb
}

func NewPersonBuilder() *PersonBuilder {
	return &PersonBuilder{&Person{}}
}

func (b *PersonBuilder) Build() *Person {
	return b.person
}

func main() {
	pb := NewPersonBuilder()
	pb.Lives().At("123 London Road").In("London").Postcode("SW123BC").Works().At("Fabrikam").AsA("Programmer").Earning(123000)
	person := pb.Build()
	fmt.Println(person)
}
