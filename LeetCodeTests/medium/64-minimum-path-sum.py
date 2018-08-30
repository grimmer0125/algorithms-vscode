# https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms
class Solution:
    # ~ leetcode-198-house-robber
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

def test_func():
    test = Solution()
    assert test.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert test.minPathSum([[0]]) == 0
