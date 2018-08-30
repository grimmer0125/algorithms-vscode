# https://leetcode.com/problems/generate-parentheses/solution/
# the code of its Appraoch 3. closure number way is hard to understand

# Approach 2: Backtracking
class Solution:
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S, left, right):
            if left == N and left == right:
                ans.append(S)
            if left < N:
                backtrack(S+"(", left+1, right)
            if right < left:
                backtrack(S+")", left, right+1)
        backtrack("", 0, 0)
        return ans

def test_func():
    test = Solution()
    ans = test.generateParenthesis(3)
    # FIXME: improve the comparision to dispite the order
    assert ans == ["((()))", "(()())","(())()","()(())","()()()"]
