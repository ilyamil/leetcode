#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> char_to_idx;

    int left = -1;
    int right = 0;
    int length = 0;
    while (right != s.length()) {
        if (char_to_idx.find(s[right]) != char_to_idx.end()
            && char_to_idx[s[right]] > left) {
            left = char_to_idx[s[right]];
        }
        char_to_idx[s[right]] = right;
        length = max(length, right - left);
        right++;
    }
    return length;
}

int main() {
    // string s = "bbbbb";
    // std::cout << lengthOfLongestSubstring(s);

    string s = "abcabcbb";
    std::cout << lengthOfLongestSubstring(s);
}