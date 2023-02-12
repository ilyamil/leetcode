#include <iostream>
#include <vector>
#include <string>

using namespace std;


void populate(vector<string> &a, string str, int left_cnt, int right_cnt) {
    if (left_cnt == 0 && right_cnt == 0) {
        a.push_back(str);
        return;
    }
    if (right_cnt > 0) {
        populate(a, str + ')', left_cnt, right_cnt - 1);
    }
    if (left_cnt > 0) {
        populate(a, str + '(', left_cnt - 1, right_cnt + 1);
    }
}


vector<string> generateParenthesis(int n) {
    vector<string> ans;
    populate(ans, "", n, 0);
    return ans;
}


int main() {
    int N = 2;
    auto parenthesis = generateParenthesis(N);
    for (auto &p : parenthesis) {
        cout << p << ' ';
    }
}