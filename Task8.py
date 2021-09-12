class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        if len(s) == 0:
            return 0
        
        # Убираем ведущие пробелы
        Spases = True
        i = 0
        while Spases and i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                Spases = False
                
        # проверяем знак
        if s[i] == '+' or s[i] == '-':
            res.append(s[i])
            i += 1
        digits = False
        
        # проверяем число
        while i < len(s):
            if s[i].isdigit():
                digits = True
                res.append(s[i])
                i += 1
            else:
                break

        # Если цифр не встретилось
        if not digits:
            return 0
        
        # Анализируем цифры
        res = int(''.join(res))
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        elif res < - (2 ** 31):
            res = - (2 ** 31)
        
        return res


import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_myAtoi(self):
        Enter = '42'
        out = 42
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)
        
    def test_2_myAtoi(self):
        Enter = '   -42'
        out = -42
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)
        
    def test_3_myAtoi(self):
        Enter = '   +42'
        out = 42
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)
        
    def test_4_myAtoi(self):
        Enter = '4193 with words'
        out = 4193
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)
        
    def test_5_myAtoi(self):
        Enter = 'words and 987'
        out = 0
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)

    def test_6_myAtoi(self):
        Enter = '-91283472332'
        out = -2147483648
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)
        
    def test_7_myAtoi(self):
        Enter = '91283472333'
        out = 2 ** 31 - 1
        answer = Solution()
        self.assertEqual(answer.myAtoi(Enter), out)

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
