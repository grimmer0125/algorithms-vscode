# https://leetcode.com/problems/climbing-stairs/solution/ has a faster way
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0] * (n+1)
        dp[2]=2
        dp[1]=1
        if n>= 3:
            for i in range(3,(n+1)):
                print(i)
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

def test_func():
    test = Solution()
    assert test.climbStairs(2) == 2
    assert test.climbStairs(3) == 3
