class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        total = len(nums)
        if total == 0:
            return [-1, -1]
        elif target > nums[-1]:
            return [-1, -1]
        elif target < nums[0]:
            return [-1, -1]

        find_start = -1
        find_end = -1
        if nums[0] == target:
            find_start = 0
        if nums[total-1] == target:
            find_end = total-1
        # try binary search
        def find_first_occurrence(forward):
            start = 0
            end = total-1
            find = -1
            while True:
                dif = end-start
                if dif == 1:
                    break
                cursor = start + dif//2
                if nums[cursor] > target:
                    end = cursor
                elif nums[cursor] == target:
                    find = cursor
                    if forward:
                        end = cursor
                    else:
                        start = cursor
                else:
                    start = cursor
            return find
        if find_start == -1:
            find_start = find_first_occurrence(True)
        if find_end == -1:
            find_end = find_first_occurrence(False)

        if find_start == -1:
            find_start = find_end
        if find_end == -1:
            find_end = find_start
        return [find_start, find_end]
def test_func():
    nums = [5,7,7,8,8,10]
    test = Solution()
    assert test.searchRange(nums, 8) == [3,4]
    assert test.searchRange(nums, 6) == [-1,-1]
    assert test.searchRange([1,3], 1) == [0,0]
