#include <iostream>
#include <vector>

using namespace std;

void populate(vector<vector<int>>& ans, vector<int>& nums, vector<int>& current, int start, int max_size) {
    if (current.size() == max_size) {
        ans.push_back(current);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        current.push_back(nums[i]);
        populate(ans, nums, current, i + 1, max_size);
        current.pop_back();
    }
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> ans = {};
    vector<int> current;
    for (int i = 0; i <= nums.size(); i++) {
        populate(ans, nums, current, 0, i);
    }
    return ans;
}

int main() {
    vector<int> nums = {1, 2, 3};
    auto s = subsets(nums);
    for (auto el: s) {
        for (auto e: el) {
            cout << e << ' ';
        }
        cout << endl;
    }
}