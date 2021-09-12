class Solution:
    def longestCommonPrefix(self, strs):
        if '' in strs:
            return ''
        res = ''
        common = True
        Minimal_Word = min(strs, key=len)
        for i in range(len(Minimal_Word)):
            for word in strs:
                if Minimal_Word[i] != word[i]:
                    return res
            res += Minimal_Word[i]
        return res
        
             

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_longestCommonPrefix(self):
        enter = ['flight', 'flower', 'flu']
        out = 'fl'
        answer = Solution()
        self.assertEqual(answer.longestCommonPrefix(enter), out)
        
    def test_2_longestCommonPrefix(self):
        enter = ['car', 'cars', 'dog']
        out = ''
        answer = Solution()
        self.assertEqual(answer.longestCommonPrefix(enter), out)
        
    def test_3_longestCommonPrefix(self):
        enter = ['car', '', 'can']
        out = ''
        answer = Solution()
        self.assertEqual(answer.longestCommonPrefix(enter), out)
        
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
