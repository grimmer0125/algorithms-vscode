class Solution:
    # Given a collection of distinct integers, return all possible permutations.
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Backtracking, ~ leetcode-22
        ans = []
        def permute2(a, nums):
            total = len(nums)
            for i in range(0, total):
                if total == 1:
                    num = nums[i]
                    a.append(num)
                    # O(n! * n)
                    ans.append(a.copy()) # O(n), n = len(nums), some people use [[]] + [], make many new lists
                    a.pop()
                else:
                    #             K
                    # n!->(n*n),(n-1)*(n-1) due to pop/insert
                    # total O((n!)^2*n)
                    num = nums.pop(i) # some people use [0:i-1]+[i+1:]
                    a.append(num)
                    permute2(a, nums)
                    nums.insert(i, num) # O(k), k<n
                    a.pop()
        permute2([],nums)
        return ans

# should be faster than
# https://leetcode.com/problems/permutations/discuss/163037/Simple-Python-Recursion
# https://leetcode.com/problems/permutations/discuss/164091/Python-Recursive-Solution

# same as https://leetcode.com/problems/permutations/discuss/164496/Beats-87.93-of-python3-submissions...Backtracking

# ? slower than iterative: https://leetcode.com/problems/permutations/discuss/162729/Beat-99-python-iterative-solution-with-explanation?
# should not differ too much
#
def test_func():
    test = Solution()
    assert test.permute([1,2,3]) == [ [1,2,3], [1,3,2], [2,1,3],
                                      [2,3,1], [3,1,2], [3,2,1]]
