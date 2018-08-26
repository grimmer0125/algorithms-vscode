# https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
# Your code should preferably run in O(n) time and use only O(1) memory.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if headA == None or headB == None:
            return None

        if headA == headB:
            return headA

        markA = headA
        markB = headB
        finalA = None
        finalB = None
        terminate = False
        while terminate == False:
            if headA.next == None:
                if finalA == None:
                    finalA = headA
                    headA = markB
                else:
                    terminate = True
            else:
                headA = headA.next
            if headB.next == None:
                if finalB == None:
                    finalB = headB
                    headB = markA
                else:
                    terminate = True
            else:
                headB = headB.next
            if headA == headB:
                if finalA == finalB:
                    return headA
                else:
                    return None
def test_func():
    test = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1_b = ListNode(7)
    node2_b = ListNode(8)
    node3_b = ListNode(9)
    node1_b.next = node2_b
    node2_b.next = node3_b
    node3_b.next = node3
    assert test.getIntersectionNode(node1, node1_b) == node3
    node1_b = node1
    assert test.getIntersectionNode(node1, node1_b) == node1
