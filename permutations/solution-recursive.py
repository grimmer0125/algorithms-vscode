#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
from functools import reduce
import operator as op

def find_next_levels_ways(n_target, cur_total):
    ways = 0
    for number in range(1, 7): # [1, 6]
        # print("number:{}".format(number))
        pseudo_total = cur_total + number
        if pseudo_total ==  n_target:
            ways+=1
            break
        else:
            # print("ok, go to next level")
            ways += find_next_levels_ways(n_target, pseudo_total)
    return ways

# recursive is slower 
if __name__ == '__main__':
    total = find_next_levels_ways(10,0)
    print(total)
