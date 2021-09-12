class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            # сначала проверяем палиндром симметричный относительно одной буквы
            left = i
            right = i
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            res.append([len(s[left + 1:right]), s[left + 1:right]])
            # потом проверяем палиндром, симметричный относительно пары соседних букв
            if i < len(s) - 1 and s[i] == s[i+1]:
                left = i
                right = i + 1
                while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                    left -= 1
                    right += 1
                res.append([len(s[left + 1:right]), s[left + 1:right]])
        if len(res) == 0:
            return s[0]
        max_len = res[0][0]
        result = res[0][1]
        for i in range(len(res)):                # пробегаем по списку палиндромов
            if res[i][0] > max_len:  # находим максимальное значение длины палиндрома
                max_len = res[i][0]
                result = res[i][1]   # и запоминаем его значение
        return result



        
import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_longest_substr(self):
        s = 'babad'
        r = 'bab'
        answer = Solution()
        self.assertEqual(answer.longestPalindrome(s), r)

    def test_2_longest_substr(self):
        s = 'cbbd'
        r = 'bb'
        answer = Solution()
        self.assertEqual(answer.longestPalindrome(s), r)
                         
    def test_3_longest_substr(self):
        s = 'a'
        r = 'a'
        answer = Solution()
        self.assertEqual(answer.longestPalindrome(s), r)
        
    def test_4_longest_substr(self):
        s = 'ac'
        r = 'a'
        answer = Solution()
        self.assertEqual(answer.longestPalindrome(s), r)
        
    def test_5_longest_substr(self):
        s = '"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"'
        answer = Solution()
        print(answer.longestPalindrome(s))
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
