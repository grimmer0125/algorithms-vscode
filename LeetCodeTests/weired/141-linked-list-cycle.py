# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# somehow this solution # input: [3,2,0,-4] tail connects to node index 1
# test is failed on LeetCode: Time Limit Exceeded
# Solution2 is no problem. Also this problems has no Python3 supprot on LeetCode
# Also, Approach 2 (two pointers) of https://leetcode.com/problems/linked-list-cycle/solution/ is weired, why not use the below solution
class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        first_id = id(head)
        head = head.next
        while head:
            if id(head) == first_id:
                return True
            head = head.next
        return False

class Solution2:
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
