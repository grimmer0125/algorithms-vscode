# Design a stack that supports push, pop, top, and
# retrieving the minimum element in constant time.

# TODO: : use heap to improve the speed of push/pop. heap: O(logn)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.min = None # or float('-inf')

    # O(n)
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.min = min(self.queue)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.queue): # if self.queue
            # TODO: pop -> del
            self.queue.pop(len(self.queue)-1)
            if len(self.queue):
                # O(n)
                # TODO: add if top == self.min:
                self.min = min(self.queue)
            else:
                self.min = None

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue):
            return self.queue[-1]
        else:
            return None

    # O(1)
    def getMin(self):
        """
        :rtype: int
        """
        return self.min

def test_func():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
