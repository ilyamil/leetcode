#include <iostream>
#include <vector>

using namespace std;

int maxSubArray(vector<int>& nums) {
    // Time complexity: O(n)
    // Space: O(n)
    vector<int> dp(nums.size(), nums[0]);
    int max_sum = dp[0];
    for (int i = 1; i < dp.size(); i++) {
        dp[i] = nums[i] + (dp[i - 1] > 0? dp[i - 1]: 0);
        max_sum = max(dp[i], max_sum);
    }
    return max_sum;
}

int main() {
    // -2,  1, -3, 4, -1, 2, 1, -5, 4
    // -2, -1, -4, 0, -1, 1, 2, -3, 1
    //  1,  3,  2, 5,  1, 2, 0, -1, 4

    // 5,   4, -1,  7,  8
    // 5,   9,  8, 15, 23
    // 23, 18, 14, 15,  8
}