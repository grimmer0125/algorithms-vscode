# https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
import numpy as np

class Solution:
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
def test_func():
    test = Solution()
    # TODO: use '0' instead of 0
    a = np.array([['1', '1', '1', '1', 0],
                  ['1', '1', 0, '1', 0],
                  ['1', '1', 0, 0, 0],
                  [0, 0, 0, 0, 0]])
    b = a.tolist()
    assert test.numIslands(b) == 1
    a2 = np.array([['1', '1', 0, 0, 0],
                   ['1', '1', 0, 0, 0],
                   [0, 0, '1', 0, 0],
                   [0, 0, 0, '1', '1']])
    b2 = a2.tolist()
    assert test.numIslands(b2) == 3
