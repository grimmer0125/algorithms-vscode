class Solution:
    def calTwoSquareArea(self, K, L, M, N, P, Q, R, S):
        width1 = M - K
        height1 = N - L
        area1 = width1 * height1

        width2 = R - P
        height2 = S - Q
        area2 = width2 * height2

        intercetArea = 0
        intercetLen1 = self.getIntercet([K, M], [P, R])
        intercetLen2 = self.getIntercet([L, N], [Q, S])
        if (intercetLen1 > 0 and intercetLen2 > 0):
            intercetArea = intercetLen1 * intercetLen2

        total = area1 + area2 - intercetArea

        return total

    def getIntercet(self, line1, line2):
        intercetLen = 0

        # line1' rectangle is in the right side
        if (line1[0] <= line2[0]):
            #line2'range is within line1's range
            if (line1[1] >= line2[1]):
                intercetLen = line2[1] - line2[0]
            else:
                intercetLen = line1[1] - line2[0]
                if (intercetLen < 0):
                    intercetLen = 0
        elif (line2[1] >= line1[1]):
            #line1'range is within line2's range
            intercetLen = line1[1] - line1[0]
        else:
            intercetLen = line2[1] - line1[0]
            if (intercetLen < 0):
                intercetLen = 0
        return intercetLen
def test_func():
    test = Solution()
    assert test.calTwoSquareArea(-4, 1, 2, 6, 0, -1, 4, 3) == 42
