#include <iostream>
#include <vector>

using namespace std;

int lower_bound(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    int mid = (left + right) / 2;
    while (left <= right) {
        if (nums[mid] >= target) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
        mid = (left + right) / 2;
    }
    return left;
}


vector<int> searchRange(vector<int>& nums, int target) {
    if (nums.size() == 0) {
        return {-1, -1};
    }
    if (nums.size() == 1) {
        if (nums[0] == target) {
            return {0, 0};
        }
        else {
            return {-1, -1};
        }
    }

    int lb = lower_bound(nums, target);
    int ub = lower_bound(nums, target + 1) - 1;
    if (lb < nums.size() && nums[lb] == target) {
        return {lb, ub};
    }
    return {-1, -1};
}

int main() {
    // vector<int> a = {5,7,7,8,8,10};
    // vector<int> ans = searchRange(a, 8); // [3, 4]

    // vector<int> a = {1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7};
    // vector<int> ans = searchRange(a, 3);

    // vector<int> a = {1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7};
    // vector<int> ans = searchRange(a, 6);

    // vector<int> a = {1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7};
    // vector<int> ans = searchRange(a, 7);

    // vector<int> a = {1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7};
    // vector<int> ans = searchRange(a, 1);

    // vector<int> a = {1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7};
    // vector<int> ans = searchRange(a, 1);

    // vector<int> a = {1, 2};
    // vector<int> ans = searchRange(a, 3);

    vector<int> a = {2, 2};
    vector<int> ans = searchRange(a, 2);

    cout << ans[0] << ' ' << ans[1];
    // [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7]
}