package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func parseInput(filename string) ([][]int, error) {
	contents, err := os.ReadFile(filename)
	if err != nil {
		return [][]int{}, err
	}

	lines := strings.Split(string(contents), "\n")

	reports := make([][]int, len(lines)-1)
	for i, report := range lines[:len(lines)-1] {
		levels := strings.Split(report, " ")
		reports[i] = make([]int, len(levels))

		for j, level := range levels {
			levelInt, err := strconv.Atoi(level)
			if err != nil {
				return [][]int{}, err
			}

			reports[i][j] = levelInt
		}
	}

	return reports, nil
}

func isSafe(report []int) bool {
	prevDir := 0
	prevLevel := 0
	prevDiff := 0

	isSafe := true
	for _, level := range report {
		if prevDiff == 0 && prevLevel == 0 {
			prevLevel = level
			continue
		}

		diff := prevLevel - level

		dir := 1
		if diff > 0 {
			dir = -1
		}

		if prevDir != 0 && dir != prevDir {
			isSafe = false
			break
		}

		absDiff := math.Abs(float64(diff))
		if absDiff > 3 || absDiff < 1 {
			isSafe = false
			break
		}

		prevDir = dir
		prevLevel = level
		prevDiff = diff
	}

	return isSafe
}

func main() {
	reports, err := parseInput("input")
	if err != nil {
		log.Fatal(err)
	}

	var safeReportCount int
	for _, report := range reports {
		isSafe := isSafe(report)
		if isSafe {
			safeReportCount++
		}

		fmt.Printf("%t %#v\n", isSafe, report)
	}

	fmt.Println(safeReportCount)
}
