# 415. Add Strings
# Given two non-negative integers num1 and num2 represented as string, 
# return the sum of num1 and num2.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str: 
        num1_array = [] 
        num2_array = []        
        for c1 in num1: 
            num1_array.append(int(c1))
        for c2 in num2: 
            num2_array.append(int(c2))
        
        sum_array = [] 
        sum_from_lower = 0
        for i in range(0, max(len(num1), len(num2))): # [0, 10)
            j1 = len(num1) - i - 1
            j2 = len(num2) - i - 1
            if j1 >=0 :
                num1_i = num1_array[len(num1) - i - 1]
            else:
                num1_i = 0
            if j2 >=0 :                      
                num2_i = num2_array[len(num2) - i - 1] 
            else:
                num2_i  = 0    
            tmp_sum = 0 
            if num1_i >= 0:
                tmp_sum += num1_i
            if num2_i >= 0:
                tmp_sum += num2_i    
            tmp_sum += sum_from_lower     
            if tmp_sum >= 10: 
                sum_from_lower = 1
                tmp_sum -= 10 
            else:
                sum_from_lower = 0                        
            sum_array.append(tmp_sum)

        if sum_from_lower > 0:
            sum_array.append(1)

        # convert to string, e.g. [1,2,3] => "321"
        s = ""
        for i in range(0, len(sum_array)):
            s += str(sum_array[len(sum_array)-i-1])
        return s        
        
def test_func():    
    test = Solution()
    assert test.addStrings("498", "547") == "1045"
    assert test.addStrings("9", "99") == "108"

