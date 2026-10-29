class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        total = rows * cols


        l = 0
        r = total


        while l <= r:
            m = (l + r) // 2
            ROWS = m // rows
            COLS = m % cols
            if ROWS == len(matrix) or COLS == len(matrix):
                return False
            if target < matrix[ROWS][COLS]:
                r = m - 1
            elif target > matrix[ROWS][COLS]:
                l = m + 1
            else:
                return True

        return False