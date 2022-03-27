package main

import (
	"bufio"
	"fmt"
	"os"
)

func get_basin_size(m [][]int, e [][]bool, i int, j int) int {

	if e[i][j] || m[i][j] == 9 {
		return 0
	}

	e[i][j] = true
	size := 1
	if i-1 >= 0 {
		size += get_basin_size(m, e, i-1, j)
	}
	if i+1 < len(m) {
		size += get_basin_size(m, e, i+1, j)
	}
	if j-1 >= 0 {
		size += get_basin_size(m, e, i, j-1)
	}
	if j+1 < len(m[0]) {
		size += get_basin_size(m, e, i, j+1)
	}
	return size
}

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("ERROR: can't open file")
	}
	defer f.Close()

	height_map := [][]int{}
	evaluated_map := [][]bool{}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		text := scanner.Text()
		line := []int{}
		for i := 0; i < len(text); i++ {
			line = append(line, int(text[i]-48))
		}
		height_map = append(height_map, line)
		evaluated_map = append(evaluated_map, make([]bool, len(line)))
	}

	basin_sizes := [3]int{0, 0, 0}
	for i := 0; i < len(height_map); i++ {
		for j := 0; j < len(height_map[0]); j++ {
			if evaluated_map[i][j] == true {
				continue
			}
			if height_map[i][j] == 9 {
				continue
			}
			size := get_basin_size(height_map, evaluated_map, i, j)
			for i, nb := range basin_sizes {
				if size > nb {
					basin_sizes[i] = size
					break
				}
			}
		}
	}
	fmt.Println(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
}
