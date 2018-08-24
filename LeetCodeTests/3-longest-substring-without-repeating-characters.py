class Solution:
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
