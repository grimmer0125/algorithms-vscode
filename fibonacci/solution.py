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

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print(fibonacci(int(sys.argv[1])))
