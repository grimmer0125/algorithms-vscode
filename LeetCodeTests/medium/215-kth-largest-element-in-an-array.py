# correct -> heap: O(nlogK)
# wrong -> quick select: average(n), worse: n^2. but it can not handle duplicate
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60293/Share-my-Python-solution-with-QuickSelect-idea

# ~ 347.

# java: PriorityQueue but c# does not have. 
# go: https://stackoverflow.com/questions/43132743/how-does-gos-heap-interface-work
# node.js: no
# c++: 1. http://www.cs.nthu.edu.tw/~dr834314/STL/sort.html
# http://www.cplusplus.com/reference/algorithm/partial_sort/ heap
# 2. nth_element. avg: O(N), worst: n^2 (depends on compilers, not defined quick sort or merge). 
# https://stackoverflow.com/a/14157584/7354486 (2013)
# https://stackoverflow.com/a/29146718/7354486 (2015)

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heap sort
        return heapq.nlargest(k, nums)[k-1]
        
def test_func():
    test = Solution()
    assert test.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert test.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4