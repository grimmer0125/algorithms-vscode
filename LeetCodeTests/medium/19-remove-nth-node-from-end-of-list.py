# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        count = 0
        while node:
            count += 1
            node = node.next

        # 1, 2 ,3 , 4, 5
        if n <= count:
            n_index = count-n
            if n_index == 0:
                # remove the first one
                head = head.next
            else:
                target_pre = n_index - 1
                # iterate again
                node = head
                index = -1
                while node:
                    index += 1
                    if index == target_pre:
                        node.next = node.next.next
                        return head
                    node = node.next
        return head
def test_func():
    test = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    test.removeNthFromEnd(node, 2)
    assert node.next.next.next.val == 5
    assert node.next.next.next.next is None
