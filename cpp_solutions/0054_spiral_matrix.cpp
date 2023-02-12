#include <iostream>
#include <vector>

using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    int N = matrix.size();
    int M = matrix[0].size();
    vector<int> ans;
    int left = 0;
    int right = M - 1;
    int top = 0;
    int bot = N - 1;
    // 1 -> left to right
    // 2 -> top to bottom
    // 3 -> right to left
    // 4 -> bottom to top
    int direction = 1;
    while (left <= right && top <= bot) {
        if (direction == 1) {
            for (int i = left; i <= right; i++) {
                ans.push_back(matrix[top][i]);
            }
            top++;
            direction = 2;
        }
        else if (direction == 2) {
            for (int i = top; i <= bot; i++) {
                ans.push_back(matrix[i][right]);
            }
            right--;
            direction = 3;
        }
        else if (direction == 3) {
            for (int i = right; i >= left; i--) {
                ans.push_back(matrix[bot][i]);
            }
            bot--;
            direction = 4;
        }
        else if (direction == 4) {
            for (int i = bot; i >= top; i--) {
                ans.push_back(matrix[i][left]);
            }
            left++;
            direction = 1;
        }
    }

    return ans;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    for (auto el: spiralOrder(matrix)) {
        cout << el << ' ';
    }
}