class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if ispalindrom(s):
            return s
        palindroms = []                                     # создаем список всех подстрок-палиндромов
        for i in range(len(s) - 1):
            for j in range((i + 1), len(s)):
                if ispalindrom(s[i:j+1]):
                    palindroms.append([len(s[i:j+1]), s[i:j+1]])
        if len(palindroms) == 0:
            return s[0]
        max_len = palindroms[0][0]
        result = palindroms[0][1]
        for i in range(len(palindroms)):                # пробегаем по списку палиндромов
            if palindroms[i][0] > max_len:  # находим максимальное значение длины палиндрома
                max_len = palindroms[i][0]
                result = palindroms[i][1]   # и запоминаем его значение
        return result
        
def ispalindrom(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True




        
import unittest

class Tests_Solution(unittest.TestCase):
        
##    def test_1_longest_substr(self):
##        s = 'babad'
##        r = 'bab'
##        answer = Solution()
##        self.assertEqual(answer.longestPalindrome(s), r)
##
##    def test_2_longest_substr(self):
##        s = 'cbbd'
##        r = 'bb'
##        answer = Solution()
##        self.assertEqual(answer.longestPalindrome(s), r)
##                         
##    def test_3_longest_substr(self):
##        s = 'a'
##        r = 'a'
##        answer = Solution()
##        self.assertEqual(answer.longestPalindrome(s), r)
##        
##    def test_4_longest_substr(self):
##        s = 'ac'
##        r = 'a'
##        answer = Solution()
##        self.assertEqual(answer.longestPalindrome(s), r)
        
    def test_5_longest_substr(self):
        s = '"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"'
        answer = Solution()
        print(answer.longestPalindrome(s))
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
