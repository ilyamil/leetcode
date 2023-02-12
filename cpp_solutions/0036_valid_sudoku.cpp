#include <iostream>
#include <vector>

using namespace std;

bool isValidSudoku(vector<vector<char>>& board) {
    // check if rows are valid
    for (auto& row: board) {
        vector<int> counter(9);
        for (auto c: row) {
            if (c == '.') {
                continue;
            }
            counter[c - '0' - 1]++;
            if (counter[c - '0' - 1] > 1) {
                return false;
            }
        }
    }
    // check if cols are valid
    for (int col = 0; col < 9; col++) {
        vector<int> counter(9);
        for (int row = 0; row < 9; row++) {
            if (board[row][col] == '.') {
                continue;
            }
            counter[board[row][col] - '0' - 1]++;
            if (counter[board[row][col] - '0' - 1] > 1) {
                return false;
            }            
        }
    }
    // check if squares are valid
    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) {
            vector<int> counter(9);
            for (auto i = 0 + x * 3; i < (3 + x * 3); i++) {
                for (auto j = 0 + y * 3; j < (3 + y * 3); j++) {
                    if (board[i][j] == '.') {
                        continue;
                    }
                    counter[board[i][j] - '0' - 1]++;
                    if (counter[board[i][j] - '0' - 1] > 1) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

int main() {

}