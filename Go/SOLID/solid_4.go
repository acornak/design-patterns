// SOLID principles
// 4: Interface segregation principle

package main

type Document struct {
}

type Machine interface {
	Print(d Document)
	Fax(d Document)
	Scan(d Document)
}

type MultiFunctionPrinter struct {
}

func (m MultiFunctionPrinter) Print(d Document) { panic("not implemented") }

func (m MultiFunctionPrinter) Fax(d Document) { panic("not implemented") }

func (m MultiFunctionPrinter) Scan(d Document) { panic("not implemented") }

type OldFashionedPrinter struct{}

func (o OldFashionedPrinter) Print(d Document) {
	panic("not implemented")
}

// Deprecated:
func (o OldFashionedPrinter) Fax(d Document) {
	panic("operation not supported")
}
func (o OldFashionedPrinter) Scan(d Document) {
	panic("operation not supported")
}

// ISP taken into account
type Printer interface {
	Print(d Document)
}

type Scanner interface {
	Scan(d Document)
}

type Fax interface {
	Fax(d Document)
}

type MyPrinter struct{}

func (m MyPrinter) Print(d Document) {}

type Photocopier struct{}

func (p Photocopier) Scan(d Document) {}

func (p Photocopier) Print(d Document) {}

type MultiFunctionDevice interface {
	Printer
	Scanner
	Fax
}

type MultiFunctionMachine struct {
	printer Printer
	scanner Scanner
	fax     Fax
}

func (m MultiFunctionMachine) Print(d Document) {
	m.printer.Print(d)
}

func (m MultiFunctionMachine) Scan(d Document) {
	m.scanner.Scan(d)
}

func (m MultiFunctionMachine) Fax(d Document) {
	m.fax.Fax(d)
}

func main() {}
