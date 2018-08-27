# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next_ = 0
        node = None
        rHeadNode = None
        while l1 or l2 or next_:
            if node is None:
                node = ListNode(0)
                rHeadNode = node
            else:
                node.next = ListNode(0)
                node = node.next
            sum_ = next_ + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            current_ = sum_ % 10
            if sum_ >= 10:
                next_ = 1
            else:
                next_ = 0
            node.val = current_
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return rHeadNode

def test_func():
    test = Solution()
    node1 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)

    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(4)
    sum_node = test.addTwoNumbers(node1, node2)
    assert sum_node.val == 7
    assert sum_node.next.val == 0
    assert sum_node.next.next.val == 8

    node3 = ListNode(5)
    node4 = ListNode(5)
    sum_node = test.addTwoNumbers(node3, node4)
    assert sum_node.val == 0
    assert sum_node.next.val == 1
