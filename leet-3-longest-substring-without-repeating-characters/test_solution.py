from solution import Solution

def test_func():
    test = Solution()
    assert test.lengthOfLongestSubstring("abcabcbb") == 3
    assert test.lengthOfLongestSubstring("pwwkew") == 3
    assert test.lengthOfLongestSubstring("bbbbb") == 1
    assert test.lengthOfLongestSubstring(" ") == 1
    assert test.lengthOfLongestSubstring("dvdf") == 3
