class Solution:
    # the below way is similar to the 2nd/3rd way mentioned in
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
    # , which is so called Sliding Window. But
    # 1. our way uses "find" which is O(n)
    # 2. that article uses hashset whose worse case is still O(n), not O(1)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLen = 0
        charList = ""

        for i in range(0, len(s)):
            char = s[i]
            find_index = charList.find(char)
            if find_index>=0:
                tmp_len = len(charList)
                if tmp_len > maxLen:
                    maxLen = tmp_len
                if find_index == len(charList)-1:
                    # reset all
                    charList = ""
                else:
                    charList = charList[(find_index+1):]
            charList += char
            if i == len(s)-1:
                tmp_len = len(charList)
                if tmp_len > maxLen:
                    maxLen = tmp_len
        return maxLen

def test_func():
    test = Solution()
    assert test.lengthOfLongestSubstring("abcabcbb") == 3
    assert test.lengthOfLongestSubstring("pwwkew") == 3
    assert test.lengthOfLongestSubstring("bbbbb") == 1
    assert test.lengthOfLongestSubstring(" ") == 1
    assert test.lengthOfLongestSubstring("dvdf") == 3
