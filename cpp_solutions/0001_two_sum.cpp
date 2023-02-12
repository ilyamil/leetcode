#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> key_idx = {{nums[0], 0}};
    for (auto i = 1; i < nums.size(); i++) {
        if (key_idx.find(target - nums[i]) != key_idx.end()) {
            return {key_idx[target - nums[i]], i};
        }
        else {
            key_idx[nums[i]] = i;
        }
    }
    return {-1, -1};
}

int main() {
    vector<int> nums1 = {1, 2, 10, 20};
    int target1 = 21;
    auto ans1 = twoSum(nums1, target1);
    cout << ans1[0] << ' ' << ans1[1];
}