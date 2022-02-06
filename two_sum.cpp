#include <iostream>
#include <vector>
#include <unordered_map>


std::unordered_map<int, std::vector<int>> create_hash_map(std::vector<int>& nums) {
    std::unordered_map<int, std::vector<int>> hm;
    for (int i = 0; i < nums.size(); i++) {
        if (hm.count(nums[i]) == 0) {
            hm[nums[i]] = std::vector<int>{i};
        }
        else {
            hm[nums[i]].push_back(i);
        }
    }
    return hm;
}

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, std::vector<int>> num_indices = create_hash_map(nums);
    int diff, first, second = -1;
    for (int i = 0; i < nums.size(); i++) {
        diff = target - nums[i];
        if (num_indices.count(diff) == 1) {
            first = i;
            if (diff != nums[i]) {
                second = num_indices[diff][0];
                break;
            }
            else {
                if (num_indices[diff].size() > 1) {
                    second = num_indices[diff][1];
                    break;
                }
            }
        }
    }
    return {first, second};
}


int main() {
    std::vector<int> nums = {3, 2, 4};
    int target = 6;
    auto a = twoSum(nums, target);
    for (auto el: a) {
        std::cout << el << " " << std::endl;
    }
}