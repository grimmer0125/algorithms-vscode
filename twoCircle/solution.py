# http://jwilson.coe.uga.edu/EMAT6680Su12/Carreras/EMAT6690/Essay2/essay2.html
import math
class Solution:
    def calTwoCircleArea(self, x1, y1, r1, x2, y2, r2):
        centerD = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
        if ((r1 + r2) < centerD):
            return 0
        r1sq = r1 * r1
        r2sq = r2 * r2

        # one circle is inside another circle
        if (r1 >= r2 and abs(r1 - r2) >= centerD):
            return math.pi * r2sq
        elif (r1 < r2 and abs(r1 - r2) >= centerD):
            return math.pi * r1sq

        # overlap, get interception area
        theta1 = (math.acos((r1sq + (centerD * centerD) - r2sq) / (2 * r1 * centerD))) * 2
        theta2 = (math.acos((r2sq + (centerD * centerD) - r1sq) / (2 * r2 * centerD))) * 2
        area1 = 0.5 * r1sq * (theta1 - math.sin(theta1))
        area2 = 0.5 * r2sq * (theta2 - math.sin(theta2))

        return area1 + area2
def test_func():
    test = Solution()
    # 5.137166941154073
    assert 0 <= abs(test.calTwoCircleArea(2, 2, 3, 5, 5, 3)-5.137) <=  0.001
