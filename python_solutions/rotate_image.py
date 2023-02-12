from typing import List


def transpose(matrix: List[List[int]]) -> None:
    N = len(matrix)
    for row_idx in range(N):
        for col_idx in range(row_idx, N):
            matrix[col_idx][row_idx], matrix[row_idx][col_idx] = \
                matrix[row_idx][col_idx], matrix[col_idx][row_idx]


def mirror(matrix: List[List[int]]) -> None:
    N = len(matrix)
    for row_idx in range(N):
        for col_idx in range(N//2):
            matrix[row_idx][col_idx], matrix[row_idx][N - col_idx - 1] = \
                matrix[row_idx][N - col_idx - 1], matrix[row_idx][col_idx]


def rotate(matrix: List[List[int]]) -> None:
    transpose(matrix)
    mirror(matrix)


if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    rotate(matrix)
    expected_output = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    print(matrix == expected_output)