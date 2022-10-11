#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;


// set<int> twoSum(vector<int>& nums, int target, int s) {
//     set<int> visited;
//     for (int i = s; i < nums.size(); i++) {
//         if (visited.find(target - nums[i]) == visited.end()) {
//             visited.insert(nums[i]);
//         }
//         else {
//             return {target, target - nums[i], nums[i]};
//         }
//     }
//     return {};
// }


vector<vector<int>> threeSum(vector<int>& nums) {
    // O(nlogn) + O(n) * O(n)
    sort(nums.begin(), nums.end());
    vector<vector<int>> ans;
    for (int i = 0; i < nums.size() - 2; i++) {
        int front = i + 1;
        int back = nums.size() - 1;
        while (front < back) {
            int sum = nums[i] + nums[front] + nums[back];
            if (sum > 0) {
                back--;
            }
            else if (sum < 0) {
                front++;
            }
            else {
                vector<int> triplet = {nums[i], nums[front], nums[back]};
                ans.push_back(triplet);

                while (front < back && nums[front] == triplet[1]) {
                    front++;
                }
                while (front < back && nums[back] == triplet[2]) {
                    back--;
                }
            }
        }
        while (i + 1 < nums.size() && nums[i + 1] == nums[i]) {
            i++;
        }
    }

    return ans;
}


int main() {
    // vector<int> A = {-1,0,1,2,-1,-4};
    // auto answer = threeSum(A);

    vector<int> A = {-2,0,1,1,2};
    auto answer = threeSum(A);

    for (auto a: answer) {
        for (auto el: a) {
            cout << el << ' ';
        }
        cout << endl;
    }
}