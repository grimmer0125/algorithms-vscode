class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        non_finished_brackets = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                non_finished_brackets.append(char)
            elif len(non_finished_brackets) > 0:
                if char == ')' and non_finished_brackets[-1] == '(':
                    non_finished_brackets.pop()
                elif char == ']' and non_finished_brackets[-1] == '[':
                    non_finished_brackets.pop()
                elif char == '}' and non_finished_brackets[-1] == '{':
                    non_finished_brackets.pop()
                else:
                    return False
            else:
                return False
        if len(non_finished_brackets) > 0:
            return False
        return True

def test_func():
    test = Solution()
    assert test.isValid("()") == True
    assert test.isValid("()[]{}") == True
    assert test.isValid("(]") == False
    assert test.isValid("([)]") == False
    assert test.isValid("{[]}") == True
