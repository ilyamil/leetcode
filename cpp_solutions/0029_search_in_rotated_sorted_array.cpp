#include <iostream>
#include <vector>

using namespace std;

int search(vector<int>& nums, int target) {
    int lowest = 0;
    int highest = nums.size() - 1;
    int mid = (lowest + highest) / 2;
    while (lowest < highest) {
        if (target == nums[mid]) {
            return mid;
        }
        if (nums[mid] > nums[highest]) {
            lowest = mid + 1;
        }
        else {
            highest = mid;
        }
        mid = (lowest + highest) / 2;
    }
    // mid - index of min element in an array
    if (mid == 0) {
        // array is already sorted
        lowest = 0;
        highest = nums.size() - 1;
    }
    else {
        if (target == nums[0]) {
            return 0;
        }
        else if (target > nums[0]) {
            lowest = 0;
            highest = mid - 1;
        }
        else {
            lowest = mid;
            highest = nums.size() - 1;
        }
    }

    while (lowest < highest) {
        mid = (lowest + highest) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[mid] > target) {
            highest = mid;
        }
        else {
            lowest = mid + 1;
        }
    }

    mid = (lowest + highest) / 2;
    return nums[mid] == target? mid: -1;
}

int main() {
    // vector<int> a = {4, 5, 6, 7, 8, 0, 1, 2};
    // vector<int> a = {4, 5, 6, 7, 0, 1, 2};
    // vector<int> a = { 0, 1, 2, 3, 4, 5, 6, 7, 8};
    // vector<int> a = {1, 3};
    // vector<int> a = {4, 5, 1};
    vector<int> a = {3, 5, 1};
    cout << search(a, 3);
}