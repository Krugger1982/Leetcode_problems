class Solution:
    def romanToInt(self, s: str) -> int:
        Letters = {'I':1, 'IV':4, 'V':5, 'IX':9,
                   'X':10, 'XL':40,'L':50, 'XC':90,
                   'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        res = 0
        i = 0
        while i < (len(s)):
            if i < (len(s)) - 1 and Letters[s[i]] < Letters[s[i + 1]]:
                res += Letters[s[i] + s[i + 1]]
                i += 2
            else:
                res += Letters[s[i]]
                i += 1
        return res
             

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_Roman_to_int(self):
        enter = 'I'
        out = 1
        answer = Solution()
        self.assertEqual(answer.romanToInt(enter), out)
        
    def test_2_Roman_to_int(self):
        enter = 'II'
        out = 2
        answer = Solution()
        self.assertEqual(answer.romanToInt(enter), out)
        
    def test_3_Roman_to_int(self):
        enter = 'IX'
        out = 9
        answer = Solution()
        self.assertEqual(answer.romanToInt(enter), out)
        
    def test_4_Roman_to_int(self):
        enter = 'MCMLXXXII'
        out = 1982
        answer = Solution()
        self.assertEqual(answer.romanToInt(enter), out)
        
    def test_5_Roman_to_int(self):
        enter = 'MCMXCIV'
        out = 1994
        answer = Solution()
        self.assertEqual(answer.romanToInt(enter), out)

    def test_6_Roman_to_int(self):
        enter = 'MMMMMMMMMMMMMMMMMMCCCXLV'
        out = 18345
        answer = Solution()
        self.assertEqual(answer.romanToInt(enter), out)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
