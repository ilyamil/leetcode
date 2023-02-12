#include <iostream>
#include <vector>

using namespace std;

void rotate(vector<vector<int>>& matrix) {
    int N = matrix.size();
    for (int i = 0; i < N; i++) {
        for (int j = i; j < N; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }

    for (int i = 0; i < N; i++) {
        int max = N % 2 == 1? N / 2 + 1: N / 2;
        for (int j = 0; j < max; j++) {
            swap(matrix[i][j], matrix[i][N - j - 1]);
        }
    }
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // vector<vector<int>> matrix = {
    //     {1, 2},
    //     {3, 4}
    // };

    rotate(matrix);

    for (auto row: matrix) {
        for (auto c: row) {
            cout << c << ' ';
        }
        cout << endl;
    }
}