class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        length = len(nums)        
        for i in range(0, length):
            num_i = nums[i]
            numDict[num_i] = i
        for i in range(0, length):
            num = nums[i]
            remain = target - num
            if remain in numDict:
                remain_index = numDict[remain]
                if i != remain_index:
                    return [i, remain_index]     

