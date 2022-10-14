#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> letterCombinations(string digits) {
    if (digits.size() == 0) {
        return {};
    }

    vector<vector<string>> mapping = {
        {"a", "b", "c"}, {"d", "e", "f"}, {"g", "h", "i"},
        {"j", "k", "l"}, {"m", "n", "o"}, {"p", "q", "r", "s"},
        {"t", "u", "v"}, {"x", "w", "y", "z"}
    };

    vector<int> total_comb;
    int factor = -1;
    for (auto d: digits) {
        if (d == '7' || d == '9') {
            factor = 4;
        }
        else {
            factor = 3;
        }
        if (total_comb.size() == 0) {
            total_comb.push_back(factor);
        }
        else {
            total_comb.push_back(total_comb.back() * factor);
        }    
    }

    int idx = (digits[0] - '0') - 2;
    vector<vector<string>> combinations = {mapping[idx]};
    for (int i = 1; i < digits.size(); i++) {
        int j = 0;
        int T = total_comb[i];
        vector<string> new_comb(T);
        for (auto &prev_comb: combinations.back()) {
            idx = (digits[i] - '0') - 2;
            for (auto letter: mapping[idx]) {
                new_comb[j] = prev_comb + letter;
                j++;
            }
        }
        combinations.push_back(new_comb);
    }

    return combinations.back();
}

int main() {
    string A = "4";
    auto ans = letterCombinations(A);
    for (auto c: ans) {
        cout << c << ' ';
    }
}