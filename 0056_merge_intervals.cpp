#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Time complexity: O(nlogn)
    // Space complexity: O(logn)
    if (intervals.size() == 1) {
        return intervals;
    }

    auto cmp = [](vector<int> a, vector<int> b) {return -a[0] > -b[0];};
    sort(intervals.begin(), intervals.end(), cmp);
    vector<vector<int>> ans;
    vector<int> interval = intervals[0];
    for (int i = 1; i < intervals.size(); i++) {
        if ((intervals[i][0] == interval[0] && intervals[i][1] > interval[1])
            || (intervals[i][0] <= interval[1] && intervals[i][1] > interval[1])) {
            interval[1] = intervals[i][1];
        }
        else if (intervals[i][0] > interval[1]) {
            ans.push_back(interval);
            interval[0] = intervals[i][0];
            interval[1] = intervals[i][1];
        }
        if (i == intervals.size() - 1) {
            ans.push_back(interval);
        }
    }
    return ans;
}

int main() {
    // vector<vector<int>> intervals = {{1, 3}, {2, 2}, {1, 10}, {12, 13}, {14, 15}};
    // vector<vector<int>> intervals = {{1, 3}, {14, 15}, {17, 19}};
    // vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{15,18}};
    // vector<vector<int>> intervals = {{1,4}, {5, 6}};
    vector<vector<int>> intervals = {{1,4}, {2, 3}};
    for (auto i: merge(intervals)) {
        cout << i[0] << ' ' << i[1] << endl;
    }
}