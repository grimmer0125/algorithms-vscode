// slow, should use the way in solution_fastest.py 
package main

import (
	"fmt"
	"math/big"
	"sort"
)

func calPart1(sum, numChoice5 int) (r *big.Int) {
	r = new(big.Int).MulRange(int64(numChoice5+1), int64(sum))
	return
}

func mul(a, b *big.Int) *big.Int {
	return new(big.Int).Mul(a, b)
}

func factorial(b int) *big.Int {
	return new(big.Int).MulRange(1, int64(b))
}

func calChoices(choiceList []int) (result *big.Int) {

	var sumChoices int
	for _, value := range choiceList {
		sumChoices += value
	}

	result = new(big.Int).Div(calPart1(sumChoices, choiceList[5]),
		mul(mul(mul(mul(factorial(choiceList[0]), factorial(choiceList[1])), factorial(choiceList[2])), factorial(choiceList[3])), factorial(choiceList[4])))

	// fmt.Println(result)
	return
}

func waysDiceBoardGame(nTarget, start, end int, c chan *big.Int) (numberWays *big.Int) {

	numberWays = big.NewInt(0)

	for count6 := start; count6 < end; count6++ {
		total5 := nTarget - count6*6
		// q: quotient
		q := total5 / 5
		fmt.Printf("number 6-%dth. Total number5:%d", count6, q+1)
		for count5 := 0; count5 < q+1; count5++ {
			fmt.Printf("number 5-%dth in 6th-%d\n", count5, count6)
			total4 := total5 - count5*5
			q := total4 / 4
			for count4 := 0; count4 < q+1; count4++ {
				total3 := total4 - count4*4
				q := total3 / 3
				for count3 := 0; count3 < q+1; count3++ {
					total2 := total3 - count3*3
					q := total2 / 2
					for count2 := 0; count2 < q+1; count2++ {
						total1 := total2 - count2*2
						count1 := total1

						choiceList := []int{count6, count5, count4, count3, count2, count1}

						sort.Ints(choiceList)
						choices := calChoices(choiceList)

						numberWays.Add(numberWays, choices)
						// fmt.Println(numberWays)
					}
				}
			}
		}
	}

	if c != nil {
		c <- numberWays
	}

	return numberWays
}

func startParallelEstimation(nTarget, numProcess int) (totalResults *big.Int) {
	totalResults = new(big.Int)
	q := nTarget / 6
	rangeLength := (q + 1) / numProcess

	if numProcess > 1 && rangeLength >= 1 {

		c := make(chan *big.Int, numProcess)

		for i := 0; i < numProcess; i++ {
			var start, end int
			if i != (numProcess - 1) {
				start = i * rangeLength
				end = (i + 1) * rangeLength

			} else {
				start = i * rangeLength
				end = q + 1
			}
			go waysDiceBoardGame(nTarget, start, end, c)
		}

		for i := 0; i < numProcess; i++ {
			r := <-c
			fmt.Printf("channel result:%s", r.String())
			totalResults.Add(totalResults, r)
		}

	} else {
		totalResults = waysDiceBoardGame(nTarget, 0, q+1, nil)
	}

	return
}

func main() {
	// if total steps is 10, how many ways (for a dice) to achieve it, e.g. 4->4->2
	r := startParallelEstimation(10, 1)
	fmt.Println(r)
}
