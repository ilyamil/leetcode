#include <iostream>
#include <vector>

using namespace std;

void sortColors(vector<int>& nums) {
    // 0 - red, 1 - white, 2 - blue
    vector<int> counter(3);
    for (auto el: nums) {
        counter[el]++;
    }

    int idx = 0;
    for (auto i = 0; i < 3; i++) {
        while (counter[i] > 0) {
            nums[idx] = i;
            idx++;
            counter[i]--;
        }
    }
}

int main() {
    // vector<int> nums = {2,0,2,1,1,0};
    vector<int> nums = {2};
    sortColors(nums);
    for (auto el: nums) {
        cout << el << ' ';
    }
}