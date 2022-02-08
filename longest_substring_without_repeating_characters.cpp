#include <iostream>
#include <unordered_set>
#include <string>


int lengthOfLongestSubstring(std::string s) {
    std::unordered_set<char> seen = {};
    int left = 0;
    int right = 0;
    int max_length = 0;
    while (right < s.length()) {
        if (seen.count(s[right]) == 0) {
            seen.insert(s[right]);
            if (max_length < seen.size()) {
                max_length = seen.size();
            }
            right++;
        } else {
            seen.erase(s[left]);
            left++;
        }
    }
    return max_length;
}


int main() {
    std::string test_s = "pwwkwew";
    std::cout << lengthOfLongestSubstring(test_s);
}