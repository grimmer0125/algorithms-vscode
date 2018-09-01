import bisect
# >>> bisect.bisect_left(a, 5)
# 3
# >>> bisect.bisect_right(a, 5) -1
# 5
class Solution:
    def num_complementary_pairs(self, k, a):
        complementaryTotal = 0
        a.sort()
        for i in range(0, len(a)):
            target_value = k - a[i]
            firstMatch = bisect.bisect_left(a, target_value)
            finalMatch = bisect.bisect_right(a, target_value)-1

            if firstMatch > -1:
                complementaryTotal += finalMatch - firstMatch + 1
def test_func():
    test = Solution()
    a = [1, 8, -3, 0, 1, 3, -2, 4, 5]
    test.num_complementary_pairs(6, a) == 7
