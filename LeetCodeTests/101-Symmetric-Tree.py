# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        currentLevel = []
        nextLevel = []

        if (root.left == None) != (root.right == None):
             return False
        elif root.left == None:
            return True

        currentLevel.append(root.left)
        currentLevel.append(root.right)

        while len(currentLevel)>0:
            count = len(currentLevel)
            for i in range(0, count):
                node_x = currentLevel[i]

                if node_x == None:
                    continue

                if i<= count/2:
                    j = count-1-i
                    node_y = currentLevel[j]
                    if node_x.val != node_y.val:
                        return False
                    if (node_x.left == None) != (node_y.right == None):
                        return False
                    if (node_x.right == None) != (node_y.left == None):
                        return False
                nextLevel.append(node_x.left)
                nextLevel.append(node_x.right)
            currentLevel = nextLevel
            nextLevel = []
        return True

def test_func():
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert test.isSymmetric(root) == True
    root.left.left = None
    root.left.right = TreeNode(3)
    root.right.left = None
    assert test.isSymmetric(root) == False
