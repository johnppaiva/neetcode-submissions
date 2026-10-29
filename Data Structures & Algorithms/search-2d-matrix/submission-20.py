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
            print(ROWS,COLS)
            if target == matrix[ROWS][COLS]:
                return True
            elif target < matrix[ROWS][COLS]:
                r = m - 1
            else:
                l = m + 1

        return False