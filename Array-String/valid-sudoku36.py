''' Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules. '''


## Compare every row first for duplicate then column and then start with boxes.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Row check
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s: return False
                if item != ".": s.add(item)
        
        # Column check
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s: return False
                if item != ".": s.add(item)

        # Box check
        box = [(0,0), (3,0), (6,0), (0,3), (0,6), (3,3), (3,6), (6,3), (6,6)]
        for i, j in box:
            s = set()
            for row in range(i,i+3):
                for col in range(j, j+3):
                    item = board[col][row]
                    if item in s: return False
                    if item != ".": s.add(item)
        
        return True
