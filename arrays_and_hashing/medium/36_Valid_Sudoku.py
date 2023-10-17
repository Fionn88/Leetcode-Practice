"""
Runtime
104ms
Beats 49.65% of users with Python3

Memory
16.14MB
Beats 95.42% of users with Python3
"""
# Time Complexity：O(n^2)
# Space Complexity：O(1)
# Approach 1 ：Check for duplicate numbers in the vertical, horizontal, and 3x3 grid.
def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for duplicate numbers in the vertical
        for row in board:
            dup = {x for x in row if row.count(x) > 1}
            if '.' in dup:
                dup.remove('.')
            if dup:
                return False 

        # Check for duplicate numbers in the horizontal
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            dup = {x for x in column if column.count(x) > 1}
            if '.' in dup:
                dup.remove('.')
            if dup:
                return False 

        # Check for duplicate numbers in the 3x3 grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                dup = {x for x in square if square.count(x) > 1}
                if '.' in dup:
                    dup.remove('.')
                if dup:
                    return False 
        return True