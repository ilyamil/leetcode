from typing import List


def dfs(board, word, row, col, count):
    if count == len(word):
        return True

    if (row < 0) or (row >= len(board)) or (col < 0) or (col >= len(board[0]))\
        or (word[count] != board[row][col]):
        return False

    tmp = board[row][col]
    board[row][col] = ''
    found = dfs(board, word, row + 1, col, count + 1)\
        or dfs(board, word, row - 1, col, count + 1)\
        or dfs(board, word, row, col + 1, count + 1)\
        or dfs(board, word, row, col - 1, count + 1)
    board[row][col] = tmp

    return found


def exist(board: List[List[str]], word: str) -> bool:
    N = len(board)
    M = len(board[0])

    for i in range(N):
        for j in range(M):
            if board[i][j] == word[0] and dfs(board, word, i, j, 0):
                return True
    
    return False


if __name__ == '__main__':
    pass