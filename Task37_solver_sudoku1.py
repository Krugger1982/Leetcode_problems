# +ПРобегаем по всем ячейкам в первый раз, все щначения "." заменяем на "123456789" (все варианты) - назовем их "ячейки с вариантами"
# +Ввелем переменную, changed = False (по умолчанию)
# +Начинаем бегать по доске. 
# +**  Если в очередной ячейке цифра, то такую цифру надо вычеркнуть из всех ячеек с вариантами  - в этой строке
#                                                                                               - в этом столбце
#                                                                                               - в этом квадрате 3х3
#                                                                                                       грницы квадрата:    [(i//3) * 3,(i//3) * 3  + 3)
#                                                                                                                           [(j//3) * 3,(j//3) * 3  + 3)
#   Просматриваем строки: если в строке среди ячеек с вариантами какое-либо число встречается тоько один раз,
#         то из этой ячейки удаляются все остальгые цифры (она становится не "ячейкой с вариантами", а просто ячейкой с цифрой
# **      и корректируем ячейки с вариантами в строке, столбце, квадрате (как в предыдущем пункте)
#   Просматриваем столбцы (то же самое) **
#   Просматриваем квадраты (то же самое) **
# Последовательность ** вынести в отдельный метод
# после каждого изменения доски значение changed меняется на True
# Если после прохождения тела цикла changed остался False (пустой пробег, нечего менять) - выход из цикла.



class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        changed = True
        # Сначала превратим все неразгаданные ячейки в ячейки с вариантами
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = '123456789'
        count = 0
        while changed and count < 100:
            # Условие выхода - безрезультатный пробег, когда во время пробега не проведено изменений
            count += 1
            changed = False
            
# 1. освобождаем ячейки с вариантами от уже отгаданных чисел
            for i in range(9):
                for j in range(9):
                    if len(board[i][j]) == 1:       # Если в ячейке одна цифра - убираем ее из всех ячеек с вариантами
                        if self.clear_string(board, i, j)or self.clear_clmn(board, i, j) or self.clear_sbx(board, i, j):
                        # в строке, столбце или подквадрате
                            changed = True  # Если проводились какие-то изменения
                            
# 2. Освобождаем подколекцию (строку, столбец или квадрат 3х3), если в ячейках с вариантами какая-либо цифра встречается ТОЛЬКО ОДИН РАЗ
        # 2.1 В строках:
            collection = []
            for row in board:
                for ColNumber in range(9):
                    collection.append(row[ColNumber])       # делаем копию строки
                if self.clr_alone(collection):                  # вычищаем копию
                    changed = True                          # Если проводились какие-то изменения
                for ColNumber in range(9):
                    row[ColNumber] = collection[ColNumber]  # и возвращаем измененную копию обратно в строку row
                collection = []                             # и обнуляем копию
            # 2.2   В столбцах
            for ColNumber in range(9):
                for row in board:
                    collection.append(row[ColNumber])       # делаем копию столбца
                if self.clr_alone(collection):              # вычищаем копию
                    changed = True
                for rowNumber in range(9):
                    board[rowNumber][ColNumber] = collection[rowNumber] # и возвращаем измененную копию обратно в столбец
                collection = []                             # и обнуляем копию
            # 2.3 В квадратиках
            for i_square in range(3):
                for j_square in range(3):       # перебираем все квадраты 3х3
                    # внутри квадрата
                    for i in range(i_square * 3, i_square*3 + 3):
                        for j in range(j_square * 3, j_square*3 + 3):
                            collection.append(board[i][j])      # делаем копию
                    if self.clr_alone(collection):                  # вычищаем копию
                        changed = True
                    collect_index = 0
                    for i in range(i_square * 3, i_square*3 + 3):
                        for j in range(j_square * 3, j_square*3 + 3):
                            board[i][j] = collection[collect_index]     # расставляем ячейки обратно в квадрат
                            collect_index += 1
                    collection = []                                     # и обнуляем копию
        
                
    def clear_string(self, board, rowNumber, colNumber):
        cleared = False
        for currentColNumber in range(len(board[rowNumber])):
            if currentColNumber != colNumber and board[rowNumber][colNumber] in board[rowNumber][currentColNumber]:
                board[rowNumber][currentColNumber] = board[rowNumber][currentColNumber].replace(board[rowNumber][colNumber], '')
                cleared = True
        return cleared
    
    def clear_clmn(self, board, rowNumber, colNumber):
        cleared = False
        for currentRowNumber in range(len(board)):
            # перебираем строки и рассматриваем j-тый столбец в них
            if currentRowNumber != rowNumber and board[rowNumber][colNumber] in board[currentRowNumber][colNumber]:
                 board[currentRowNumber][colNumber] =  board[currentRowNumber][colNumber].replace(board[rowNumber][colNumber], '')
                 cleared = True
        return cleared
                 
    def clear_sbx(self, board, rowNumber, colNumber):
        cleared = False
        for i in range(rowNumber//3*3, rowNumber//3*3+3):
            for j in range(colNumber//3*3, colNumber//3*3+3):       # пробегаем по квадрату
                if (i, j) != (rowNumber, colNumber) and board[rowNumber][colNumber] in board[i][j]:
                    board[i][j] = board[i][j].replace(board[rowNumber][colNumber], '')
                    cleared = True
        return cleared

    def clr_alone(self, collection):
        Changed = False
        for i in range(1,10):
            if str(i) in collection:
                continue
            count = 0
            for cell in collection:
                if len(cell) > 1 and str(i) in cell:
                    count += 1
#            print('i=', i, 'количество', count)
            if count == 1:
                for currentcell in range(len(collection)):
                    if len(collection[currentcell]) > 1 and str(i) in collection[currentcell]:
                        collection[currentcell] = str(i)
                        Changed = True
        return Changed

    def clr_double(self, collection):
        Changed = False
        double = None
        for cell in collection:
            if len(cell) == 2 and collection.count(cell) == 2:
                print(cell)
                double = cell
                break
        for cell in collection:
            if cell != double:
                for digit in double:
                    print("удаляем ", digit, end=' ')
                    if digit in cell:
                        print(cell, end=' ')
                        cell = cell.replace(digit, '')
                        print(cell)
                        Changed = True
        return Changed      
        
import unittest

class Tests_searchInsert(unittest.TestCase):
##    def test_clrAlone(self):
##        String = ['8', '259', '1235', '23', '356', '256', '4', '237', '37']
##        print(String)
##        ansver = Solution()
##        ansver.clr_alone(String)
##        print(String)
##        
##    def test_1_Solved_Sudoku(self):
##        board =[["5","3",".",".","7",".",".",".","."],
##                ["6",".",".","1","9","5",".",".","."],
##                [".","9","8",".",".",".",".","6","."],
##                ["8",".",".",".","6",".",".",".","3"],
##                ["4",".",".","8",".","3",".",".","1"],
##                ["7",".",".",".","2",".",".",".","6"],
##                [".","6",".",".",".",".","2","8","."],
##                [".",".",".","4","1","9",".",".","5"],
##                [".",".",".",".","8",".",".","7","9"]]
##        ansver = Solution()
##        ansver.solveSudoku(board)
##        for String in board:
##            print(String)
    def test_ClrDouble(self):
        String = ['12', '12', '123', '124', '125', '16', '7', '8', '9']
        ansver = Solution()
        ansver.clr_double(String)
        print(String)

##    def test_2_Solved_Sudoku(self):
##        board =[[".",".","9","7","4","8",".",".","."],
##                ["7",".",".",".",".",".",".",".","."],
##                [".","2",".","1",".","9",".",".","."],
##                [".",".","7",".",".",".","2","4","."],
##                [".","6","4",".","1",".","5","9","."],
##                [".","9","8",".",".",".","3",".","."],
##                [".",".",".","8",".","3",".","2","."],
##                [".",".",".",".",".",".",".",".","6"],
##                [".",".",".","2","7","5","9",".","."]]
##        ansver = Solution()
##        ansver.solveSudoku(board)
##        for String in board:
##            print(String)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
