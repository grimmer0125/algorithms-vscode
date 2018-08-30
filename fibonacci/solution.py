#!/usr/bin/env python
import sys

def fibonacci(n):
    second_last = 0
    last = 1
    last_tmp = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(2, n + 1):
            last_tmp = last
            last = last + second_last
            second_last = last_tmp
    return last

# without memorization, O(~2^n)
# https://en.wikipedia.org/wiki/Dynamic_programming#Fibonacci_sequence
def fibonacci_recursive_memorization(n):
    values = [0]*(n+1)
    visited_list = [0]*(n+1)
    def fib_recursive(n):
        if visited_list[n]:
            return values[n]
        visited_list[n] = True
        if n <= 1:
            values[n] = n
        else:
            values[n] = fib_recursive(n-1) + fib_recursive(n-2)
        return values[n]
    return fib_recursive(n)

def test_solution():
    assert fibonacci(10) == 55
    assert fibonacci_recursive_memorization(10) == 55

# if __name__ == '__main__':
#     if len(sys.argv) >= 2:
#         print(fibonacci(int(sys.argv[1])))
