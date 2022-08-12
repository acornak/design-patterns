// SOLID principles
// 1: Single-responsibility principle

package main

import (
	"fmt"
	"io/ioutil"
	"net/url"
	"strings"
)

var entryCount = 0

type Journal struct {
	entries []string
}

func (j *Journal) AddEntry(text string) int {
	entryCount++
	entry := fmt.Sprintf("%d: %s", entryCount, text)
	j.entries = append(j.entries, entry)

	return entryCount
}

func (j *Journal) RemoveEntry(index int) {
	j.entries = append(j.entries[:index], j.entries[index+1:]...)
}

// separation of concerns
// God Object = antipattern

func (j *Journal) String() string {
	return strings.Join(j.entries, "\n")
}

func (j *Journal) Save(filename string) {
	_ = ioutil.WriteFile(filename, []byte(j.String()), 0644)
}

func (j *Journal) Load(filename string) {
	// ...
}

func (j *Journal) LoadFromWeb(url *url.URL) {
	// ...
}

// solution
var LineSeparator = "\n"

func SaveToFile(j *Journal, filename string) {
	_ = ioutil.WriteFile(filename, []byte(strings.Join(j.entries, LineSeparator)), 0644)
}

// even better
type Persistence struct {
	lineSeparator string
}

func (p *Persistence) SaveToFile(j *Journal, filename string) {
	_ = ioutil.WriteFile(filename, []byte(strings.Join(j.entries, p.lineSeparator)), 0644)
}

func main() {
	j := Journal{}
	j.AddEntry("This is the first entry.")
	j.AddEntry("Second day is also boring.")
	fmt.Println(j.String())

	// SaveToFile(&j, "journal.txt")

	p := Persistence{"/r/n"}
	p.SaveToFile(&j, "journal.txt")
}
