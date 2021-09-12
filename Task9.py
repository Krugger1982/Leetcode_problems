class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        Copy = x
        # сначала определим сколько разрядов в числе x 
        N = 0
        while x > 0:    
            x //= 10
            N += 1
        x = Copy
        
        while N > 1:
            print(x, N)
            # теперь сравним левую и правую цифры
            if x // (10 ** (N - 1)) != x % 10:
                return False
            # и отрежем левую и правую цифры
            x = x % (10 ** (N-1))
            x = x // 10
            N -= 2
        return True
            
            
            




        

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_isPalindrome(self):
        answer = Solution()
        entrance = 121
        output = True
        self.assertEqual(answer.isPalindrome(entrance), output)

    def test_2_isPalindrome(self):
        answer = Solution()
        entrance = -121
        output = False
        self.assertEqual(answer.isPalindrome(entrance), output)

    def test_3_isPalindrome(self):
        answer = Solution()
        entrance = 10
        output = False
        self.assertEqual(answer.isPalindrome(entrance), output)

    def test_4_isPalindrome(self):
        answer = Solution()
        entrance = -101
        output = False
        self.assertEqual(answer.isPalindrome(entrance), output)

    def test_5_isPalindrome2(self):
        answer = Solution()
        entrance = 121
        output = True
        self.assertEqual(answer.isPalindrome2(entrance), output)

    def test_6_isPalindrome2(self):
        answer = Solution()
        entrance = -121
        output = False
        self.assertEqual(answer.isPalindrome2(entrance), output)

    def test_7_isPalindrome2(self):
        answer = Solution()
        entrance = 10
        output = False
        self.assertEqual(answer.isPalindrome2(entrance), output)

    def test_8_isPalindrome2(self):
        answer = Solution()
        entrance = -101
        output = False
        self.assertEqual(answer.isPalindrome2(entrance), output)

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
