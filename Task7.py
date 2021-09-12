class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = - int(str(- x)[::-1])
        if res > 2 ** 31 - 1  or res < - 2 ** 31:
            return 0
        return res


        
import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_reverce_int(self):
        answer = Solution()
        x = 123
        y = 321
        self.assertEqual(answer.reverse(x), y)

    
    def test_2_reverce_int(self):
        answer = Solution()
        x = -123
        y = -321
        self.assertEqual(answer.reverse(x), y)

    def test_3_reverce_int(self):
        answer = Solution()
        x = 2 ** 32
        y = 0
        self.assertEqual(answer.reverse(x), y)

    def test_4_reverce_int(self):
        answer = Solution()
        x = -(2 ** 32)
        y = 0
        self.assertEqual(answer.reverse(x), y)

    def test_5_reverce_int(self):
        answer = Solution()
        x = 8463847412
        y = 0
        self.assertEqual(answer.reverse(x), y)

    def test_6_reverce_int(self):
        answer = Solution()
        x = -9463847412
        y = 0
        self.assertEqual(answer.reverse(x), y)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
