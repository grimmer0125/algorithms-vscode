# https://leetcode.com/problems/longest-palindromic-substring/solution/
# has a faster way
# dynamic-programming
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        start_max = 0
        end_max = 0

        total = len(s)
        for i in range(0, total-1): # bb
            # match = False
            start = i
            end = i
            while (start-1) >= 0 and (end+1) < total:
                if s[start-1] != s[end+1]:
                    # match = False
                    break
                else:
                    start -= 1
                    end += 1
                    # match = True
                    # len_ = 2*j+1
            start1 = start
            end1 = end

            # if match is False:
            # try again
            if s[i] == s[i+1]:
                start = i
                end = i+1
                # match = True
                while (start-1) >= 0 and (end+1) < total:
                    if s[start-1] != s[end+1]:
                        # match = False
                        break
                    else:
                        start -= 1
                        end += 1
                        # match = True
            if (end1-start1) > (end-start):
                start = start1
                end = end1
            if end-start > 0:
                len_ = end-start+1
                if len_ > (end_max-start_max+1):
                    end_max = end
                    start_max = start
        if end_max > 0:
            return s[start_max:(end_max+1)]
        else:
            return s[0] # "ac"
def test_func():
    test = Solution()
    assert test.longestPalindrome("a") == "a"
    assert test.longestPalindrome("ac") == "a"
    assert test.longestPalindrome("bb") == "bb"
    assert test.longestPalindrome("aaaa") == "aaaa"
    assert test.longestPalindrome("babad") == "bab"
    assert test.longestPalindrome("cbbd") == "bb"
    assert test.longestPalindrome("abcbe") == "bcb"
