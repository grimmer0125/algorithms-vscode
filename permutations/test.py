#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
from functools import reduce
import operator as op

from multiprocessing import Process, Queue

def cal_part1(n, r):
    num = reduce(op.mul, range(n, r, -1), 1)
    return num

def cal_choices(choice_list):
    l = choice_list
    f = math.factorial
    sum_choices = sum(l)
    combination = cal_part1(sum_choices, l[5])//(f(l[0])*f(l[1])*f(l[2])*f(l[3])*f(l[4]))

    return combination

def ways_dice_board_game(n_target, partition, result_queue=None):
    number_ways = 0
    print("print partition:{}".format(partition))
    for count6 in partition:
        total5 = n_target - count6*6
        # q: quotient
        q = total5//5
        print("number 6-{}th. Total number5:{}".format(count6, q+1))
        for count5 in range(0, q+1):
            print("number 5-{}th in 6th-{}".format(count5, count6))
            total4 = total5 - count5*5
            q = total4//4
            for count4 in range(0, q+1):
                total3 = total4 - count4*4
                q = total3//3
                for count3 in range(0, q+1):
                    total2 = total3 - count3*3
                    q = total2//2
                    for count2 in range(0, q+1):
                        total1 = total2 - count2*2
                        count1 = total1
                        choice_list = [count6, count5, count4, count3, count2, count1]
                        choice_list.sort()
                        choices = cal_choices(choice_list)
                        number_ways += choices
    if result_queue is not None:
        print("put result in queue:{}".format(number_ways))
        result_queue.put(number_ways)
    print("finish ways_dice_board_game")
    return number_ways

def start_parallel_estimation(n_target=10, num_process=2):
    """ Start a estimation for number of dice steps,
        this function is mainly for parallelism

    Keyword arguments:
        n_target -- target "n" spaces away from the starting point (default 10)
        num_process -- number of processes to speedup by parallelism
    """

    total_results = 0
    q = n_target//6  # q may be zero
    print("q:{}".format(q))
    range_length = (q+1)//num_process
    if num_process > 1 and range_length >= 1:
        result_queue = Queue()
        workers = []
        print("total {} workers".format(num_process))
        for i in range(0, num_process):
            if i != (num_process-1):
                partition = range(i*range_length, (i+1)*range_length)
            else:
                partition = range(i*range_length, q+1)
            d = Process(target=ways_dice_board_game, args=(n_target, partition, result_queue))
            workers.append(d)

        for worker in workers:
            worker.start()

        print("start to wait process result, total:{}".format(len(workers)))

        for worker in workers:
            data = result_queue.get()
            print("get a process result")

            total_results += data

        print("join processes")

        for worker in workers:
            worker.join()
            print("after a process join")
    else:
        partition = range(0, q+1)
        total_results = ways_dice_board_game(n_target, partition)

    return total_results

if __name__ == '__main__':
    print("start estimation")
    if len(sys.argv) >= 2:
        result = start_parallel_estimation(int(sys.argv[1]))
        print(result)
    else:
        # for testing
        result = start_parallel_estimation(10, num_process=1)
    print("total result:{}".format(result))
