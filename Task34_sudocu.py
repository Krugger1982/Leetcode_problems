class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Сначала проставим вместо точек возможные варианты цифр для неразгаданных ячеек
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    board[row][col] = [1,2,3,4,5,6,7,8,9]
        changed = True
        # Флаг для проверки последней итерации. Если доска на последнем круге изменилась, то стоит еще раз пробежаться по ней
        while changed:
            # Условие выхода из цикла - это напрасный проход, то есть все разгадано или улучшить доску нельзя
            changed = False
            deleting_unnecessary(board, changed)           # функция, вычеркивающая из неразгаданных клеток лишник цифры
            self.guessed_numbers(board, changed)           # функция для замены списка на номер в разгаданной ячейке
            
def deleting_unnecessary(board, changed):
    for row in range(len(board)):
        for col in range(len(board[row])):
            # пробегаем по каждой ячейке
            cell = board[row][col]
            if isinstance(cell, str): # если в ячейке содержится число
                # пробегаем по доске - вычеркиваем все значения cell из неразгаданных ячек
                # сначала пробегаем по строке
                for current in board[row]:
                    if isinstance(current, list) and int(cell) in current:
                        current.remove(int(cell))
                        changed = True
                # затем пробегаем по колонке
                for row_number in range(len(board)):
                    if isinstance(board[row_number][col], list) and int(cell) in board[row_number][col]:
                        board[row_number][col].remove(int(cell))
                        changed = True
                # затем пробегаем по сектору
                for sector_row in range(3*(row//3), 3*(row//3+1)):
                    for sector_col in range(3*(col//3), 3*(col//3+1)):
                        if isinstance(board[sector_row][sector_col], list) and int(cell) in board[sector_row][sector_col]:
                            board[sector_row][sector_col].remove(int(cell))
                            changed = True
    return board, changed
                                
    def guessed_numbers(self, board, changed):
        # Пробегаем по всем ячейкам
        for row in range(len(board)):
            for col in range(len(row)):
                if isinstance(board[row][col], list) and len(board[row][col]) == 1:
                    board[row][col] = str(board[row][col][0])
                    changed = True
        
            
            
        



import unittest
        
class Tests_Solution(unittest.TestCase):
    
    def test_1_deleting_unnecessary(self):
        enter = [["5","3","4"],
                 [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
                 [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]]
        changed = False
        out = [["5","3","4"],
               [[1,2,6,7,8,9],[1,2,6,7,8,9],[1,2,6,7,8,9]],
               [[1,2,6,7,8,9],[1,2,6,7,8,9],[1,2,6,7,8,9]]]
        z = deleting_unnecessary(enter, changed)
        print(z[0])
        print(z[1])
##        for i in range(len(z)):
##            for j in range(len(z[i])):
##                self.assertEqual(z[i][j], out[i][j])

##    def test_x_solveSudoku(self):
##        enter = [["5","3",".",".","7",".",".",".","."],
##                 ["6",".",".","1","9","5",".",".","."],
##                 [".","9","8",".",".",".",".","6","."],
##                 ["8",".",".",".","6",".",".",".","3"],
##                 ["4",".",".","8",".","3",".",".","1"],
##                 ["7",".",".",".","2",".",".",".","6"],
##                 [".","6",".",".",".",".","2","8","."],
##                 [".",".",".","4","1","9",".",".","5"],
##                 [".",".",".",".","8",".",".","7","9"]]
##        
##        out = [["5","3","4","6","7","8","9","1","2"],
##               ["6","7","2","1","9","5","3","4","8"],
##               ["1","9","8","3","4","2","5","6","7"],
##               ["8","5","9","7","6","1","4","2","3"],
##               ["4","2","6","8","5","3","7","9","1"],
##               ["7","1","3","9","2","4","8","5","6"],
##               ["9","6","1","5","3","7","2","8","4"],
##               ["2","8","7","4","1","9","6","3","5"],
##               ["3","4","5","2","8","6","1","7","9"]]
##        
##        answer = Solution
##        z = answer.solveSudoku(enter)
##        
##        self.assertEqual(z, out)
##
##        self.assertEqual(z, out)

# реализовать функцию "угадал цифру если
#  есть в списке данной ячейки и больше ее нет в списках строки/столбца/сектора
# перевести функцию удление лишних в метод для решения солюшн
# оттестить
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
