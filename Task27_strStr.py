class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for index in range(len(haystack)):
            if haystack[index] != needle[0]:
                continue
            else:
                if haystack[index:index+len(needle)] == needle:
                    return index
            
        return -1    

        
import unittest

class MyTests(unittest.TestCase):

    def test_1(self):
        haystack = 'hello'
        needle = 'll'
        out = 2
        answer = Solution()
        k = answer.strStr(haystack, needle)
        self.assertEqual(out, k)
        

    def test_2(self):
        haystack = ''
        needle = ''
        out = 0
        answer = Solution()
        k = answer.strStr(haystack, needle)
        self.assertEqual(out, k)

    def test_3(self):
        haystack = 'hello'
        needle = 'la'
        out = -1
        answer = Solution()
        k = answer.strStr(haystack, needle)
        self.assertEqual(out, k)

    def test_4(self):
        haystack = 'hello'*1000000 + 'helloga' + 'hello'*100
        needle = 'helloga'
        out = 5000000
        answer = Solution()
        k = answer.strStr(haystack, needle)
        self.assertEqual(out, k)

    def test_5(self):
        haystack = 'a'
        needle = 'a'
        out = 0
        answer = Solution()
        k = answer.strStr(haystack, needle)
        self.assertEqual(out, k)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
