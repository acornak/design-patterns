package main

import (
	"fmt"
	"strings"
)

type GraphicObject struct {
	Name, Color string
	Children    []GraphicObject
}

func (g *GraphicObject) String() string {
	sb := strings.Builder{}
	g.print(&sb, 0)
	return sb.String()
}

func (g *GraphicObject) print(sb *strings.Builder, depth int) {
	sb.WriteString(strings.Repeat("*", depth))
	if len(g.Color) > 0 {
		sb.WriteString(g.Color)
		sb.WriteString(" ")
	}
	sb.WriteString(g.Name)
	sb.WriteString("\n")

	for _, child := range g.Children {
		child.print(sb, depth+1)
	}
}

func NewCirlce(color string) *GraphicObject {
	return &GraphicObject{"Circle", color, nil}
}

func NewSquare(color string) *GraphicObject {
	return &GraphicObject{"Square", color, nil}
}

func main() {
	drawing := GraphicObject{"Drawing", "", nil}
	drawing.Children = append(drawing.Children, *NewCirlce("Red"))
	drawing.Children = append(drawing.Children, *NewSquare("Yellow"))

	group := GraphicObject{"Group 1", "", nil}
	group.Children = append(group.Children, *NewCirlce("Blue"))
	group.Children = append(group.Children, *NewSquare("Blue"))

	drawing.Children = append(drawing.Children, group)

	fmt.Println(drawing.String())

}
