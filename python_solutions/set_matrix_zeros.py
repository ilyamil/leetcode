from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    N = len(matrix)
    M = len(matrix[0])
    # check if any zeroes in first row or column
    is_zeroes_in_first_row = any([el == 0 for el in matrix[0]])
    is_zeroes_in_first_col = any([el[0] == 0 for el in matrix[:]])
    # set flags to first row or column if there is zeroes in matrix
    # (except first row or column)
    for row_idx in range(1, N):
        for col_idx in range(1, M):
            if not matrix[row_idx][col_idx]:
                matrix[0][col_idx] = 0
                matrix[row_idx][0] = 0

    for row_idx in range(1, N):
        if matrix[row_idx][0] == 0:
            for col_idx in range(1, M):
                matrix[row_idx][col_idx] = 0
    for col_idx in range(1, M):
        if matrix[0][col_idx] == 0:
            for row_idx in range(1, N):
                matrix[row_idx][col_idx] = 0

    if is_zeroes_in_first_row:
        for col_idx in range(0, M):
            matrix[0][col_idx] = 0
    if is_zeroes_in_first_col:
        for row_idx in range(0, N):
            matrix[row_idx][0] = 0


if __name__ == '__main__':
    test_cases = [
        {
            'input': [[1,0]],
            'output': [[0, 0]]
        },
        {
            'input': [
                [1],
                [0]
            ],
            'output': [
                [0],
                [0]
            ]
        },
        {
            'input': [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ],
            'output': [
                [1,0,1],
                [0,0,0],
                [1,0,1]
            ]
        },
        {
            'input': [
                [0,1,1],
                [1,0,1],
                [1,1,1]
            ],
            'output': [
                [0,0,0],
                [0,0,0],
                [0,0,1]
            ]
        },
        {
            'input': [
                [0,1,2,0],
                [3,4,5,2],
                [1,3,1,5]
            ],
            'output': [
                [0,0,0,0],
                [0,4,5,0],
                [0,3,1,0]
            ]
        }
    ]
    for test_case in test_cases:
        mat = test_case['input']
        setZeroes(mat)
        assert mat == test_case['output']
