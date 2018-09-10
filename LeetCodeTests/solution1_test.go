package main

import "testing"

func TestSomething(t *testing.T) {
    r := twoSum([]int{3, 2, 4}, 6)
    // Todo: use assert.Equal instead https://github.com/stretchr/testify
    if r[0] != 1 {
        t.Error("something wrong")
    }

    if r[1] != 2 {
        t.Error("something wrong")
    }
}
