class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        historyMaxProfit = 0

        minIndex = 0 # local, not global
        maxIndex = 0 # local, not global

        num_total = len(prices)
        for i in range(1, num_total):
            saved_minIndex = minIndex
            saved_maxIndex = maxIndex

            reCalculateProfit = False
            if i == num_total-1:
                reCalculateProfit = True

            if prices[i]-prices[maxIndex] >= 0:
                maxIndex = i
                saved_maxIndex = i
            elif prices[i]-prices[minIndex] < 0:
                # change local min/max range
                minIndex = i
                maxIndex = i
                reCalculateProfit = True

            if reCalculateProfit:
                if saved_maxIndex > saved_minIndex: # e.g. [7,6,5]
                    localDiff = prices[saved_maxIndex] - prices[saved_minIndex]
                    if localDiff > historyMaxProfit:
                        historyMaxProfit = localDiff
        print(historyMaxProfit)
        return historyMaxProfit

def test_func():
    test = Solution()
    assert test.maxProfit([7,1,5,3,6,4]) == 5
    assert test.maxProfit([7,6,4,3,1]) == 0
    assert test.maxProfit([1,2]) == 1
    assert test.maxProfit([1,7,2,4]) == 6
    assert test.maxProfit([2,4,1]) == 2
