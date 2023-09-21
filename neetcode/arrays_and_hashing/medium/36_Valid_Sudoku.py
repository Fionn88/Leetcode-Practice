"""
Runtime
104ms
Beats 49.65%of users with Python3

Memory
16.14MB
Beats 95.42%of users with Python3
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dup = {x for x in row if row.count(x) > 1}
            try:
                dup.remove('.')
            except:
                pass 
            if dup:
                return False 

        for col in range(9):
            column = [board[row][col] for row in range(9)]
            dup = {x for x in column if column.count(x) > 1}
            try:
                dup.remove('.')
            except:
                pass 
            if dup:
                return False 

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                dup = {x for x in square if square.count(x) > 1}
                try:
                    dup.remove('.')
                except:
                    pass 
                if dup:
                    return False 
        return True