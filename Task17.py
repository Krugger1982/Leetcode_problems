
class Solution:
    def letterCombinations(self, digits):
        result = []
        if len(digits) == 0:
            return result        
        for digit in digits:
            result = self.words(result, digit)
        return result
            


    def words(self, List_Words, digit):
        res = []
        Letters = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
                   '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        if len(List_Words) == 0:
            for Letter in Letters[digit]:
                res.append(Letter)
        else:
            for Word in List_Words:
                for Letter in Letters[digit]:
                    res.append(Word + Letter)
        return res






import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_threeSumClosest(self):
        enter = "2"
        out =  ["a","b","c"]
        answer = Solution()
        z = answer.letterCombinations(enter)
        self.assertEqual(z, out)

    def test_2_threeSumClosest(self):
        enter = '23'
        out =  ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        answer = Solution()
        z = answer.letterCombinations(enter)
        self.assertEqual(z, out)

    def test_3_threeSumClosest(self):
        enter = ''
        out =  []
        answer = Solution()
        z = answer.letterCombinations(enter)
        self.assertEqual(z, out)


if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
