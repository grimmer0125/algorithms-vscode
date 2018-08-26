# ~ 347.
import heapq

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for num in nums: # ~  collections.Counter
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        # or just iterate the key, value. linear time            
        max_list = heapq.nlargest(1, numDict, key=lambda x: numDict[x]) # ~Counter.most_common(k)
        return max_list[0]

def test_func():
    test = Solution()
    assert test.majorityElement([3,2,3]) == 3
    assert test.majorityElement([2,2,1,1,1,2,2]) == 2
