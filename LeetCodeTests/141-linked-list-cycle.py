# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# This problems has no Python3 supprot on LeetCode
# There is also a two pointers solution,
# https://leetcode.com/problems/linked-list-cycle/solution/
class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        map = {}
        while head:
            if id(head) in map:
                return True
            else:
                map[id(head)] = True
            head = head.next
        return False

def test_func():
    test = Solution()
    node1 = ListNode(1)
    assert test.hasCycle(node1) == False
    node1.val = 3
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    assert test.hasCycle(node1) == True
