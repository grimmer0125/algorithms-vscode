# throw a dice, similar to https://leetcode.com/problems/climbing-stairs/description/
# Dynamic Programming
def solution_fastest(n):
    dp = [0] * (n+1)
    dp[6]=32
    dp[5]=16
    dp[4]=8
    dp[3]=4
    dp[2]=2
    dp[1]=1
    if n>= 7:
        for i in range(7,(n+1)):
            print(i)
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]
    # print(dp[n])
    return dp[n]
