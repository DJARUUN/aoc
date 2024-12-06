package main

import (
	"bytes"
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

	contentsLF := bytes.ReplaceAll(contents, []byte("\r\n"), []byte("\n"))
	lines := strings.Split(string(contentsLF), "\n")

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

	isSafe := true
	for _, level := range report {
		if prevLevel == 0 {
			prevLevel = level
			continue
		}

		diff := prevLevel - level
		dir := 1
		if diff > 0 {
			dir = -1
		}

		absDiff := math.Abs(float64(diff))

		isSafeDir := prevDir == 0 || dir == prevDir
		isSafeDiff := absDiff > 0 && absDiff < 4

		if !isSafeDir || !isSafeDiff {
			isSafe = false
			break
		}

		prevDir = dir
		prevLevel = level
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
