#include <iostream>
#include <vector>

using namespace std;

void populate(vector<vector<int>>& target, vector<int>& source, int k) {
    if (k == source.size()) {
        target.push_back(source);
        return;
    }
    for (int i = k; i < source.size(); i++) {
        swap(source[i], source[k]);
        populate(target, source, k + 1);
        swap(source[i], source[k]);
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> ans;
    populate(ans, nums, 0);
    return ans;
}

int main() {
    vector<int> source = {1, 2, 3};
    for (auto comb: permute(source)) {
        for (auto el: comb) {
            cout << el << ' ';
        }
        cout << '\n';
    }
}