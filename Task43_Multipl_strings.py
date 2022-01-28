class Solution:
    def multiply(self, num1, num2):
        # Result - это список промежуточных строчек
        # rez - это промежуточная строчка при перемножении столбиком
        # single_rez - это  результат произведения одиночных цифр,
        # mem - это то, что "на ум пошло" при этом произведении
        # то есть 9 Х 9 = 81, single_rez = '1', mem = '8'
        Result = []
        for digit2 in reversed(num2):
            rez = ''
            mem = 0
            for digit1 in reversed(num1):
                single_rez = self.single_multiply(digit2, digit1)
                rez = str((single_rez + mem)% 10) + rez
                mem = (single_rez + mem) // 10
            if mem > 0:
                rez = str(mem) + rez
            Result.append(rez)
        return self.Summ(Result)

            
    def single_multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return 0
        res =  int(num1) * int(num2)
        return res

    def Summ(self, List_numbers):
        Max_length = len(List_numbers[0])
        for i in range(len(List_numbers)):
            # Сначала припишем нули в конце этих чисел в соответствии с их положением
            List_numbers[i] += '0' * i
            # И заодно найдем наибольшее количество рзрядов, то есть наибольшую "длину" числа
            if len (List_numbers[i]) > Max_length:
                Max_length = len (List_numbers[i])
        for i in range(len(List_numbers)):
            # Потом припишем лидирующие нули чтоб все слагаемые были одинаковой длины
            if len(List_numbers[i]) < Max_length:
                List_numbers[i] = '0' * (Max_length - len(List_numbers[i])) + List_numbers[i]
        Rezult = []
        Summa = 0
        for Razryad in range (Max_length - 1, -1, -1):   # Пробегаем по разрядам с последнего
            for Number in List_numbers:
                Summa += int(Number[Razryad])
            Rezult.append(str(Summa%10))            # Записываем очередную сумму - последний разряд
            Summa = Summa // 10                     # Запоминаем все остальные разряы суммы ("в уме")            
        if Summa > 0:
            Rezult.append(str(Summa))
        Rezult.reverse()
        Rezult = ''.join(Rezult)
        return str(int(Rezult))
             
             
            
        
import unittest

class Tests_firstMissingPositive(unittest.TestCase):
        
    def test_1_trap(self):
        N1 = '2'
        N2 = '3'
        ansver = Solution()
        self.assertEqual(ansver.multiply(N1, N2), '6')

    def test_2_trap(self):
        N1 = '15'
        N2 = '382'
        ansver = Solution()
        self.assertEqual(ansver.multiply(N1, N2), '5730')


    def test_3_trap(self):
        N1 = '0'
        N2 = '382'
        ansver = Solution()
        self.assertEqual(ansver.multiply(N1, N2), '0')        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
