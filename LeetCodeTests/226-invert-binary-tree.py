# Definition for a binary tree node.
# weird thing: You can not uncomment class TreeNode on LeetCode WebSite,
# otherwise you will get some exception
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def iterateTree(self, node):
        left = node.left
        right = node.right
        if left != None:
            node.right = TreeNode(left.val)
            node.right.left = left.left
            node.right.right = left.right
            self.iterateTree(node.right)
        else:
            node.right = None
        if right != None:
            node.left = TreeNode(right.val)
            node.left.left = right.left
            node.left.right = right.right
            self.iterateTree(node.left)
        else:
            node.left = None

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        root_clone = TreeNode(root.val)
        root_clone.left = root.left
        root_clone.right = root.right

        self.iterateTree(root_clone)
        return root_clone

def test_func():
    test = Solution()
    node1 = TreeNode(4)
    node1.left = TreeNode(2)
    node1.left.left = TreeNode(1)
    node1.left.right = TreeNode(3)
    node1.right = TreeNode(7)
    node1.right.left = TreeNode(6)
    node1.right.right = TreeNode(9)

    node2 = test.invertTree(node1)
    assert node2.left.val == 7
    assert node2.right.val == 2
    assert node2.left.left.val == 9
    assert node2.left.right.val == 6
    assert node2.right.left.val == 3
    assert node2.right.right.val == 1

    node3 = TreeNode(1)
    node3.left = TreeNode(2)
    node4 = test.invertTree(node3)
    assert node4.left == None
    assert node4.right.val == 2
