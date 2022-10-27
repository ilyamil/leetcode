#include <iostream>
#include <vector>

using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int m = matrix[0].size();
    // check are there any zeroes in first row or first column
    bool first_row_zeroes = false;
    bool first_col_zeroes = false;
    for (int i = 0; i < n; i++) {
        if (matrix[i][0] == 0) {
            first_col_zeroes = true;
        }
    }
    for (int i = 0; i < m; i++) {
        if (matrix[0][i] == 0) {
            first_row_zeroes = true;
        }
    }

    // mark rows and columns that contains zeroes
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    for (auto row: matrix) {
        for (auto el: row) {
            cout << el << ' ';
        }
        cout << endl;
    }
    // fill rows of matrix with zeroes according to the marks 
    for (int i = 1; i < n; i++) {
        if (matrix[i][0] == 0) {
            for (int j = 1; j < m; j++) {
                matrix[i][j] = 0;
            }
        }
    }
    // fill columns of matrix with zeroes according to the marks
    for (int i = 1; i < m; i++) {
        if (matrix[0][i] == 0) {
            for (int j = 1; j < n; j++) {
                matrix[j][i] = 0;
            }
        }
    }

    // fill first col and row according to flags
    if (first_col_zeroes) {
        for (int i = 0; i < n; i++) {
            matrix[i][0] = 0;
        }
    }
    if (first_row_zeroes) {
        for (int i = 0; i < m; i++) {
            matrix[0][i] = 0;
        }
    }
}

int main() {
    // vector<vector<int>> matrix = {
    //     {1,1,1},
    //     {1,0,1},
    //     {1,1,1}
    // };
    vector<vector<int>> matrix = {
        {0,1,1},
        {1,0,1},
        {1,1,1}
    };
    setZeroes(matrix);

    for (auto row: matrix) {
        for (auto el: row) {
            cout << el << ' ';
        }
        cout << endl;
    }
}