class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        total = rows * cols


        l = 0
        r = total - 1


        while l <= r:
            m = (l + r) // 2
            ROWS = m // cols
            COLS = m % cols

            if target < matrix[ROWS][COLS]:
                r = m - 1
            elif target > matrix[ROWS][COLS]:
                l = m + 1
            else:
                return True

        return False