package main

import "testing"
import (
    "math/big"
)
func TestSomething(t *testing.T) {
    r := startParallelEstimation(10, 1)
    // fmt.Println(r)
    // Todo: use assert.Equal instead https://github.com/stretchr/testify
    if r.Cmp(big.NewInt(492)) != 0 {
        t.Error("something wrong")
    }
}
