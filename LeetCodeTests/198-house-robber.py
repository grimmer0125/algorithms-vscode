# https://leetcode.com/problems/house-robber/discuss/55681/Java-O(n)-solution-space-O(1)
# https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.
# recursive way: # f(k) = max( f(k-2) + nums[k], f(k-1) )
# dynamic-programming
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        Rob = nums[0]
        NoRob = 0
        for i in range(1,len(nums)):
            temp = NoRob + nums[i]
            NoRob = max(NoRob, Rob)
            Rob = temp
        return max(Rob,NoRob)

def test_func():
    test = Solution()
    assert test.rob([1,2,3,1]) == 4
    assert test.rob([2,7,9,3,1]) == 12
