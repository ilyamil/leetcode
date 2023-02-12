from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for row in board:
        seen = set()
        for el in row:
            if el != '.' and el in seen:
                return False
            else:
                seen.add(el)
    for col_num in range(9):
        seen = set()
        for row_num in range(9):
            el = board[row_num][col_num]
            if el != '.' and el in seen:
                return False
            else:
                seen.add(el)
    for row_sq in range(3):
        for col_sq in range(3):
            seen = set()
            for row_idx in range(row_sq * 3, row_sq * 3 + 3):
                for col_idx in range(col_sq * 3, col_sq * 3 + 3):
                    el = board[row_idx][col_idx]
                    if el != '.' and el in seen:
                        return False
                    else:
                        seen.add(el)
    return True


if __name__ == '__main__':
    sudoku = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    ans = isValidSudoku(sudoku)
    print(ans)