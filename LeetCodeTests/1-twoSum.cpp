#include <vector>
#include <map>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        vector<int> r;

        map<int, int> numDict;
        int len = nums.size();
        for (int i = 0; i < len; i++) {
            int num_i = nums[i];
            numDict[num_i] = i;
        }
        for (int i = 0; i < len; i++) {
            int num_i = nums[i];
            int remain = target - num_i;
            map<int, int>::iterator iter;
            iter = numDict.find(remain);
            if(iter != numDict.end()) {
                int remain_index = iter->second;
                if (i != remain_index) {
                    
                    r.push_back(i);
                    r.push_back(remain_index);

                    // the below needs "g++" -> "clang++ -std=c++11"
                    // vector<int> v{i, remain_index};

                    break;
                }
            }
        }

        return r;
    }
};

int main() {
    cout << "1-twoSum!";

    Solution solution;
    
    vector<int> nums; 
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);
    vector<int> answer = solution.twoSum(nums, 9);
    
    int length = answer.size();    
    assert(length==2);
    assert(answer[0]==0);
    assert(answer[1]==1);

    return 0;
}
