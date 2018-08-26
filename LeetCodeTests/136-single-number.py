# https://leetcode.com/problems/single-number/solution/
# 1. extra list
# 2. dict
# 3. set
# 4. xor (^) a⊕b⊕a=(a⊕a)⊕b=0⊕b=b (correct answer)
# NOTE: :
# 2 & 3 are wrong for worse case
# 2.a (wrong) time complexity of hash table(dictionary in python) operation pop is O(1)O(1).
# 2.b (wrong) insert of py dict is also O(1)
# 3. set(nums) <= O(n)? wrong. should O(n~n^2), average O(n) to iterate all and inserta them

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

def test_func():
    test = Solution()
    assert test.singleNumber([2,2,1]) == 1
    assert test.singleNumber([4,1,2,1,2]) == 4
