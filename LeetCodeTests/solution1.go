package main

import (
	"fmt"
)

func twoSum(nums []int, target int) (ans [2]int) {
	numDict := make(map[int]int)
	length := len(nums)

	for i := 0; i < length; i++ {
		num_i := nums[i]
		numDict[num_i] = i
	}

	for i := 0; i < length; i++ {
		remain := target - nums[i]
		if remain_index, ok := numDict[remain]; ok {
			if i != remain_index {
				ans = [2]int{i, remain_index}
				return
			}
		}
	}
	return
}

func main() {
	r := twoSum([]int{3, 2, 4}, 6)
	fmt.Println(r)
}
