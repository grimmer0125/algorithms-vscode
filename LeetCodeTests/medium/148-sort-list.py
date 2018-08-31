# https://leetcode.com/problems/sort-list/discuss/46711/Python-merge-sort-with-comments.
# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# v 1 merge sort needs extra n space ? no need for linked list
# О(n) total with O(n) auxiliary, O(1) auxiliary with linked lists[1]
# 2 quick sort !! in-place. space: O(n) but time worse:n^2
# 3 heap sort(extra: O(1)). constant space complexity. but need list first, first i ~ n/2
class Solution:
    # https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F#%E5%8E%9F%E5%9C%B0%EF%BC%88in-place%EF%BC%89%E5%88%86%E5%89%B2%E7%9A%84%E7%89%88%E6%9C%AC
    def quick_sort_partition(self, left, right, pivot):
        pivotValue = pivot.val

        # swap pivot and right
        pivot.val = right.val
        right.val = pivotValue

        store = left
        store_pre = None

        # from left to right-1
        node = left
        while node and node != right:
            if node.val < pivotValue:
                # swap store & node
                tmp  = node.val
                node.val = store.val
                store.val = tmp

                # store -> store.next
                store_pre = store
                store = store.next
            node = node.next
        # swap right & store
        tmp = right.val
        right.val = store.val
        store.val = tmp
        return store, store_pre

    # can not pass leetcode's unit test since its time worse case is O(n^2)
    def quick_sort(self, left, right):
        # rightIndex > leftIndex:
        if left and right and left != right:

            # select a pivot value a[pivotIndex], choose left (head)
            pivot = left
            pivotNew, pivotNew_pre = self.quick_sort_partition(left, right, pivot)
            self.quick_sort(left, pivotNew_pre)
            if pivotNew != right:
                self.quick_sort(pivotNew.next, right)

    # TODO: implement by self later
    # merge in-place without dummy node
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        # quick sort part
        # node = head
        # while node:
        #     end = node
        #     node = node.next
        # self.quick_sort(head, end)
        # return head

        # merge sort part
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

def test_func():
    test = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    resp = test.sortList(head)
    assert resp.val == 1
    assert resp.next.val == 2
    assert resp.next.next.val == 3
    assert resp.next.next.next.val == 4

    head2 = ListNode(-1)
    head2.next = ListNode(5)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(0)

    resp = test.sortList(head2)
    assert resp.val == -1
    assert resp.next.val == 0
    assert resp.next.next.val == 3
    assert resp.next.next.next.val == 4
    assert resp.next.next.next.next.val == 5
