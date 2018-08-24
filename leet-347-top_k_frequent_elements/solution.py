import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numDict = {}
        for num in nums: # ~  collections.Counter
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        return heapq.nlargest(k, numDict, key=lambda x: numDict[x])
