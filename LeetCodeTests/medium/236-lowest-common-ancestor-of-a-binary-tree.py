# alternative: 
# dfs + stack : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.find = None
        def lowerestNode(node):
            if self.find == None:
                self.find = node

        def find_child(node, p=None, q=None):
            if node == None:
                return False

            if node == p:
                if q == None:
                    return True
                else:
                    if find_child(node.left, None, q) or find_child(node.right, None, q):
                        lowerestNode(node)
                        return True
            elif node == q:
                if p == None:
                    return True
                else:
                    if find_child(node.left, p, None) or find_child(node.right, p, None):
                        lowerestNode(node)
                        return True
            else:
                if p:
                    if q:                        
                        if find_child(node.left, p, q) or find_child(node.right, p, q):
                            return True
                        elif find_child(node.left, p, None) and find_child(node.right, None, q):
                            lowerestNode(node)
                        elif find_child(node.right, p, None) and find_child(node.left, None, q):
                            lowerestNode(node)
                    else:
                        if find_child(node.left, p, None) or find_child(node.right, p, None):
                            return True          
                else:
                    if find_child(node.left, None, q) or find_child(node.right, None, q):
                        return True                
            return False              
        find_child(root, p, q)
        return self.find

def test_func():
    test = Solution()
    node = TreeNode(3)
    node.left = TreeNode(5)
    node.left.left = TreeNode(6)
    node.left.right = TreeNode(2)
    node.left.right.left = TreeNode(7)
    node.left.right.right = TreeNode(4)
    node.right = TreeNode(1)
    node.right.left = TreeNode(0)
    node.right.right = TreeNode(8)
    assert test.lowestCommonAncestor(node, node.left, node.right) == node
    assert test.lowestCommonAncestor(node, node.left, node.left.right.right) == node.left
