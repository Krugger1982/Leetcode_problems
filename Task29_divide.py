class Solution:
    def divide(self, dividend, divisor):
        positive = dividend >= 0 and divisor >= 0 or dividend < 0 and divisor < 0       # флаг обозначающий знак результата
        if abs(divisor) == 1:
            result = abs(dividend)                        # частный случай - деление на 1
        elif abs(dividend)  < abs(divisor):               # если делимое меньше делителя - вернем 0
            result = 0
        else:
            # сначала избавимся от знаков - будем работать с абсолютными значениями
            divisor = str(abs(divisor))         
            dividend = str(abs(dividend))
            # забронируем  ячейку для результата
            result = ''     
            current = dividend[:len(divisor)]                       # отрезаем первый кусок, равный по длине делителю
            next_sign_index = len(current)                          # индекс следующей цифры 
            if int(current) <int(divisor):
                current += dividend[next_sign_index]
                next_sign_index += 1
            letter, ostatok = division(current, divisor)        # производим  деление первого куска
            result += letter                                    # записываем результат
        
            while next_sign_index < len(dividend):
                current = ostatok + dividend[next_sign_index]       # смещаем кусок
                next_sign_index += 1                                # и смещаем позицию следующей цифры
                letter, ostatok = division(current, divisor)        # производим  деление очередного куска
                result += letter                                    # записываем результат
            result = int(result)

        if  not positive:                        # добавляем в результат знак в соответствии с флагом positive
            result =  - result  
        # проверка на переполнение ответа
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
            
        return result
            
            
            
                                   

                                   
def division(a:str, b:str):
    a = int(a)
    b = int(b)
    if a < b:
        return '0', str(a)
    else:
        count = 0
        while a >= b:
            a -= b
            count += 1
        return str(count), str(a)
    
        
import unittest

class MyTests(unittest.TestCase):

    def test_1(self):
        dividend = 10
        divisor = 3
        out = 3
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_2(self):
        dividend = 7
        divisor = -3
        out = -2
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_3(self):
        dividend = 0
        divisor = 1
        out = 0
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_4(self):
        dividend = 1
        divisor = 1
        out = 1
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_5(self):
        dividend = 9
        divisor = 3
        out = 3
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_6(self):
        dividend = 2147483648
        divisor = 1
        out = 2147483647
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_7(self):
        dividend = 2147483647
        divisor = 1
        out = 2147483647
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_8(self):
        dividend = 100
        divisor = 11
        out = 9
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)

    def test_9(self):
        dividend = -2147483647
        divisor = 2
        out = - 1073741823
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)        
        
    def test_10(self):
        dividend = -1
        divisor = 1
        out = -1
        answer = Solution()
        k = answer.divide(dividend, divisor)
        self.assertEqual(out, k)       
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
