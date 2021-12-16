class Solution:
    def solveSudoku(self, M):
        """
        Do not return anything, modify board in-place instead.
        """
        def sudoku():
            R, C = len(M), len(M[0])
            for r in range(R):
                for c in range(C):
                    if M[r][c] != ".": continue
                        
                    row_values = set(int(M[r][y]) for y in range(C) if M[r][y] != ".")
                    col_values = set(int(M[x][c]) for x in range(R) if M[x][c] != ".")
                    top_left_row, top_left_col = 3*(r//3), 3*(c//3)
                    box_values = set()
                    for x in range(top_left_row, top_left_row+3):
                        for y in range(top_left_col, top_left_col+3):
                            if M[x][y] != ".":
                                box_values.add(int(M[x][y]))

                    cell_values = set(range(1,10)) - row_values - col_values - box_values
                    for val in cell_values:
                        M[r][c] = str(val)
                        if sudoku():
                            return True
                    M[r][c] = "."
                    return False
            return True
        
        sudoku()
        
import unittest

class Tests_searchInsert(unittest.TestCase):

        
    def test_1_Solved_Sudoku(self):
        board =[["5",".",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
        ansver = Solution()
        ansver.solveSudoku(board)
        for String in board:
            print(String)


    def test_2_Solved_Sudoku(self):
        print()
        board =[[".",".","9","7","4","8",".",".","."],
                ["7",".",".",".",".",".",".",".","."],
                [".","2",".","1",".","9",".",".","."],
                [".",".","7",".",".",".","2","4","."],
                [".","6","4",".","1",".","5","9","."],
                [".","9","8",".",".",".","3",".","."],
                [".",".",".","8",".","3",".","2","."],
                [".",".",".",".",".",".",".",".","6"],
                [".",".",".","2","7","5","9",".","."]]
        ansver = Solution()
        ansver.solveSudoku(board)
        for String in board:
            print(String)

##    def test_3_Solved_Sudoku_hard(self):
##        board =[["8","2",".",".",".",".","4",".","."],
##                [".","6","9",".","8",".",".",".","."],
##                [".",".",".","3",".",".",".","1","."],
##                [".",".",".",".",".","9",".",".","."],
##                [".",".",".",".",".","1","6","4","."],
##                [".",".","8",".","7",".","5",".","."],
##                [".",".",".","4","1",".",".",".","."],
##                ["4","9","2",".",".","3",".",".","."],
##                [".",".","6",".",".","8",".",".","."]]
##        ansver = Solution()
##        ansver.solveSudoku(board)
##        for String in board:
##            print(String)        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
