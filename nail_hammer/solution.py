class Solution:
    def findMaxSameHeightNails(self, a, k):
        n = len(a)
        if n == 0:
            return 0
        best = 1
        count = 1
        for i in range(0, n-1):
            if a[i] == a[i+1]:
                count += 1
            else:
                count = 0
            remaining = k if (n-1-i) > k else n-1-i
            if (count + remaining +1) > best:
                best = count + remaining +1
        return best

def test_func():
    test = Solution()
    a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
    test.findMaxSameHeightNails(a, 2) == 5
