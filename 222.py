import collections
class Solution:
    def generateParenthesis(self, n: int):
        combs, queue = [], collections.deque([(0, 0, '')])
        while queue:
            L, R, comb = queue.pop()
            if L == R == n:
                combs.append(comb)
                continue
            if L < n:
                queue.append((L+1, R, comb+'('))
            if R < L:
                queue.append((L, R+1, comb+')'))
        return combs

import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_generateParenthesis(self):
        enter = 3
        out =  ["((()))","(()())","(())()","()(())","()()()"]
        
        answer = Solution()
        z = answer.generateParenthesis(enter)
        print(z)
        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)
                


    def test_2_generateParenthesis(self):
        enter = 1
        out =  ['()']
        
        answer = Solution()
        z = answer.generateParenthesis(enter)
        print(z)
        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)
            
    def test_3_generateParenthesis(self):
        enter = 2
        out =  ['()()', '(())']
        
        answer = Solution()
        z = answer.generateParenthesis(enter)
        print(z)
        
        for i in out:
            self.assertTrue(i in z)
        for i in z:
            self.assertTrue(i in out)
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
