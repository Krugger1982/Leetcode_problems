# Валидная лоска - это доска, на которой валидны все ячейки
# Ячейки, в которых "." - валидны
# Пробегаем по каждой яцейке
# Каждую ячейку проверяяем на неповторимость 
#   - в строке
#   - в столюце
#   - в квадрате 3Х3
#       грницы квадрата:    [(i//3) * 3,(i//3) * 3  + 3)
#                           [(j//3) * 3,(j//3) * 3  + 3)
#
#
class Solution:
    def isValidSudoku(self, board):
        for i in range(9): # Это строки
            for j in range(9): # Это колонки
                if not(board[i][j] == "." or self.valid_cell(board, i, j)):
                    return False
        return True

    def valid_cell(self, board, RowNumber, ColNumber):
        return self.valid_cell_in_row(board, RowNumber, ColNumber) and self.valid_cell_in_colmn(board, RowNumber, ColNumber) and self.valid_cell_in_sbx(board, RowNumber, ColNumber)

    def valid_cell_in_row(self, board, RowNumber, ColNumber):
        return board[RowNumber].count(board[RowNumber][ColNumber]) == 1
        
    def valid_cell_in_colmn(self, board, RowNumber, ColNumber):
        for i in range(len(board)):
            if i != RowNumber and board[i][ColNumber] == board[RowNumber][ColNumber]:
                return False
        return True

    def valid_cell_in_sbx(self, board, RowNumber, ColNumber):
        for i in range(RowNumber//3*3, RowNumber//3*3+3):
            for j in range(ColNumber//3*3, ColNumber//3*3+3):
                if (i, j) != (RowNumber, ColNumber) and board[i][j] == board[RowNumber][ColNumber]:
                    return False
        return True



import unittest

class Tests_searchInsert(unittest.TestCase):
        
    def test_1_Not_Valided_Sudoku(self):
        board =[["8","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
        ansver = Solution()
        self.assertFalse(ansver.isValidSudoku(board))

    def test_2_Valided_Sudoku(self):
        board = [["5","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
        ansver = Solution()
        self.assertTrue(ansver.isValidSudoku(board))
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
