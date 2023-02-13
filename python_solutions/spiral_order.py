from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1
    order = []
    direction = 1
    while row_begin <= row_end and col_begin <= col_end:
        # 1. Left to right
        if direction == 1:
            for i in range(col_begin, col_end + 1):
                order.append(matrix[row_begin][i])
            row_begin += 1
            direction = 2
        # 2. Top to bottom
        elif direction == 2:
            for i in range(row_begin, row_end + 1):
                order.append(matrix[i][col_end])
            col_end -= 1
            direction = 3
        # 3. Right to left
        elif direction == 3:
            for i in range(col_end, col_begin - 1, -1):
                order.append(matrix[row_end][i])
            row_end -= 1
            direction = 4
        # 4. Bottom to top
        elif direction == 4:
            for i in range(row_end, row_begin - 1, -1):
                order.append(matrix[i][col_begin])
            col_begin += 1
            direction = 1
    
    return order


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    order = spiralOrder(matrix)
    print(order)
