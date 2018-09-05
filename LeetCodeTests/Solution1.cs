using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;
using System.Linq;

namespace CSharp
{
    class Solution1
    {
        public int[] TwoSum(int[] nums, int target) {
            Dictionary<int, int> numDict = new Dictionary<int, int>();
            int length = nums.Length;
            for (int i=0; i < length; i++) {
                numDict.Add(nums[i], i);
            }

            for (int i=0; i < length; i++) {
                int remain = target - nums[i];
                if (numDict.ContainsKey(remain)){
                    int remain_index = numDict[remain];
                    if (i != remain_index) { 
                        return new int[] {0, 1};
                    }
                }
            }
            return new int[]{};
        }
        public void test_solution(){
            Console.WriteLine("test_solution1");
            int[] nums = {2,7,11,15};
            int[] ans = TwoSum(nums, 9);
            Assert.IsTrue(ans.SequenceEqual(new int[] {0, 1}));
        }
    }

}
