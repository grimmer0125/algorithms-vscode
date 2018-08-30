# https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
# Approach 3:  new data structure-Threaded Binary Tree !!
# NOTE: This is a good problem and we can learn something from it
# , however, it does not explain what Inorder Traversal,
# need to figure it out first
# Preorder Traversal: Depth-first Search
# Level-order Traversal : Breath-first Search (input array is this type)
# Inorder Traversal: Depth-first Search but left->root->right
# Postorder Traversal: left->right->root

# Approach 2 (not straightforward):
# DFS but using loop + stack
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        def dfs_stack_search(root):
            while root or len(stack)>0:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        dfs_stack_search(root)
        return ans

def test_func():
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # [1,null,2,3] -> [1,3,2]
    assert test.inorderTraversal(root) == [1,3,2]
