
            
class Solution:
    def intToRoman(self, num):
        Romans = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],     # Единицы
                  ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],     # десятки
                  ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']      # сотни
                 ]
        res = ''
        for i in range(len(Romans)):
            current = num % 10
            res = Romans[i][current] + res
            num = num // 10
        res = 'M' * num + res                                                       # тысячи
        return res
       
             

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_intToRoman(self):
        enter = 1
        out = 'I'
        answer = Solution()
        self.assertEqual(answer.intToRoman(enter), out)
        
    def test_2_intToRoman(self):
        enter = 9
        out = 'IX'
        answer = Solution()
        self.assertEqual(answer.intToRoman(enter), out)

    def test_3_intToRoman(self):
        enter = 58
        out = 'LVIII'
        answer = Solution()
        self.assertEqual(answer.intToRoman(enter), out)
        
    def test_4_intToRoman(self):
        enter = 1994
        out = 'MCMXCIV'
        answer = Solution()
        self.assertEqual(answer.intToRoman(enter), out)
        
    def test_5_intToRoman(self):
        enter = 8994
        out = 'MMMMMMMMCMXCIV'
        answer = Solution()
        self.assertEqual(answer.intToRoman(enter), out)
        




        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
