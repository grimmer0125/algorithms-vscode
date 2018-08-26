# A linked list can be reversed either iteratively or recursively. 
# Could you implement both?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        preNode = None         
        while head != None:            
            next_node = head.next
            head.next = preNode
            preNode = head 
            head = next_node
        return preNode   
     
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
    rNode = test.reverseList(node1)
    assert rNode == node5
    assert node5.next == node4
    assert node4.next == node3
    assert node3.next == node2
    assert node2.next == node1
    assert node1.next == None

test_func()
