class Solution {
  twoSum(nums, target) {
    const numDict = {};
    const len = nums.length;
    for (let i = 0; i < len; i++) {
      const num_i = nums[i];
      numDict[num_i] = i;
    }
    for (let i = 0; i < len; i++) {
      const remain = target - nums[i];
      if (numDict[remain]) {
        const remain_index = numDict[remain];
        if (i !== remain_index) {
          return [i, remain_index];
        }
      }
    }
  }
}

test('', () => {
  const test = new Solution();
  const ans = test.twoSum([3, 2, 4], 6);
  expect(ans[0]).toBe(1);
  expect(ans[1]).toBe(2);
});
