package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"sync"
)

type Database interface {
	GetPopulation(name string) int
}

type singletonDatabase struct {
	capitals map[string]int
}

func (db *singletonDatabase) GetPopulation(name string) int {
	return db.capitals[name]
}

// option 1: sync.Once init() -- thread safety
// option 2: laziness using sync.Once in separate func

var once sync.Once
var instance *singletonDatabase

func readData(path string) (map[string]int, error) {
	file, err := os.Open(path)

	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	result := map[string]int{}

	for scanner.Scan() {
		k := scanner.Text()
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		result[k] = v
	}

	return result, nil
}

func GetSingletonDatabase() *singletonDatabase {
	once.Do(func() {
		db := singletonDatabase{}
		caps, err := readData("./capitals.txt")
		if err == nil {
			db.capitals = caps
		}
		instance = &db
	})
	return instance
}

// NO ABSTRACTION

// func GetTotalPopulation(cities []string) (result int) {
// 	for _, city := range cities {
// 		result += GetSingletonDatabase().GetPopulation(city)
// 	}
// 	return result
// }

func GetTotalPopulation(db Database, cities []string) (result int) {
	for _, city := range cities {
		result += db.GetPopulation(city)
	}
	return result
}

type DummyDabatase struct {
	dummyData map[string]int
}

func (d *DummyDabatase) GetPopulation(name string) int {
	if len(d.dummyData) == 0 {
		d.dummyData = map[string]int{
			"alpha": 1,
			"beta":  2,
			"gamma": 3,
		}
	}
	return d.dummyData[name]
}

func main() {
	db := GetSingletonDatabase()
	city := "Seoul"
	pop := db.GetPopulation(city)
	fmt.Printf("Population of %s = %d\n", city, pop)

	cities := []string{"alpha", "beta", "gamma"}
	// tp := GetTotalPopulation(cities)
	tp := GetTotalPopulation(&DummyDabatase{}, cities)
	fmt.Println(tp == 6)
}
