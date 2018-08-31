# https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # aaaabbb
        d=[False]*len(s)
        for i in range(len(s)):
     	    for w in wordDict:
     		    if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
     			    d[i] = True
        return d[-1]
def test_func():
    test = Solution()
    assert test.wordBreak("leetcode", ["leet", "code"]) == True
    assert test.wordBreak("applepenapple", ["apple", "pen"]) == True
    assert test.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert test.wordBreak("aaaaaaa", ["aaaa","aaa"]) == True
