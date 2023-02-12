#include <iostream>
#include <vector>

using namespace std;

bool canJump(vector<int>& nums) {
    // Time complexity: O(n)
    // Space: O(1)
    int last_pos = nums.size() - 1;
    for (int i = last_pos - 1; i >= 0; i--) {
        if (i + nums[i] >= last_pos) {
            last_pos = i;
        }
    }
    return last_pos == 0;
}

int main() {
    // 2,3,1,1,4
    // xxx--
    // -xxxx
    // --xx-
    // ----x
    vector<int> nums = {2, 0, 0, 1, 4};
    bool can = canJump(nums);
    cout << can;
}