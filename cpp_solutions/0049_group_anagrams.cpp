#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // Time complexity: O(n) * O(m*logm) = O(n*m*logm)
    unordered_map<string, vector<string>> groups;
    for (auto str: strs) {
        string str_key = str;
        sort(str_key.begin(), str_key.end());
        if (groups.find(str_key) == groups.end()) {
            groups[str_key] = {str};
        }
        else {
            groups[str_key].push_back(str);
        }
    }
    vector<vector<string>> ans;
    for (auto el: groups) {
        ans.push_back(el.second);
    }
    return ans;
}


int main() {
    vector<string> strs = {"abc", "bca", "dma"};
    // vector<string> strs = {""};
    auto groups = groupAnagrams(strs);
    for (auto g: groups) {
        for (auto an: g) {
            cout << an << ' ';
        }
        cout << endl;
    }
}