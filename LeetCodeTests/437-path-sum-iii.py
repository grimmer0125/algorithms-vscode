# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution is reference in
# https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
class Solution:
    # How many A (paths) make
    # Sum(A~G) = Target (A could be root), G is current node in helper
    # Sum(root~G) - Sum(root~A) = Target, Sum(root~G) is fixed
    # Sum(root-A) = complement = Sum(root~G)-Target <- fixed number
    def helper(self, node, target, pre_sum, cache):
        if node:
            sum_ = pre_sum + node.val

            complement = sum_ - target
            if complement in cache:
                self.result += cache[complement]

            # if not exist, set the value as 0
            cache.setdefault(sum_, 0)
            cache[sum_] += 1
            self.helper(node.left, target, sum_, cache)
            self.helper(node.right, target, sum_, cache)
            cache[sum_] -= 1
        return
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, target, 0, {0: 1})
        return self.result
def test_func():
    test = Solution()
    node = TreeNode(10)
    node.left = TreeNode(5)
    node.right = TreeNode(-3)
    node.right.right = TreeNode(11)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(2)
    node.left.right.right = TreeNode(1)
    node.left.left.left = TreeNode(3)
    node.left.left.right = TreeNode(-2)
    assert test.pathSum(node, 8) == 3
