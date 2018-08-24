from solution import Solution

def test_func():
    test = Solution()
    assert test.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
    assert test.topKFrequent([1], 1) == [1]
