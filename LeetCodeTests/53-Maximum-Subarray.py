class Solution:
    def maxSubArray(self, num_list: list[int]) -> int:    
        for index, num in enumerate(num_list):            
            if index == 0:
                global_max = num
                if num > 0: 
                    tmp_sum = num
                else:
                    tmp_sum = 0    
                continue  
            tmp_sum = tmp_sum + num
     
            if tmp_sum > global_max:
                global_max = tmp_sum 

            if tmp_sum < 0:  
                tmp_sum = 0    

        return global_max
        
        
def test_func():
    test = Solution()
    assert test.maxSubArray([3,2,6]) == 11
    assert test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert test.maxSubArray([1]) == 1
    assert test.maxSubArray([0]) == 0
    assert test.maxSubArray([-1]) == -1
    assert test.maxSubArray([-100000]) == -100000    
