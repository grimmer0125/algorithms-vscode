# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if (p == None) != (q == None):
              return False
        if p == None: # only needed for root
            return True

        if p.val != q.val:
            return False

        if (p.left == None) != (q.left == None):
            return False
        if p.left != None:
            if self.isSameTree(p.left, q.left) == False:
                return False

        if (p.right == None) != (q.right == None):
            return False
        if p.right != None:
            if self.isSameTree(p.right, q.right) == False:
                return False

        return True
def test_func():
    test = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    assert test.isSameTree(p, q) == True
    p.right.val = 1
    q.left.val = 1
    q.right.val = 2
    assert test.isSameTree(p, q) == False
    p.right = None
    q.left = None
    assert test.isSameTree(p, q) == False
