class Solution:
    def generateParenthesis(self, n):
        res = []
        if n == 0:
            return res
        if n == 1:
            return ['()']
        prev = self.generateParenthesis(n - 1)
        for permutation in prev:
            # перебираем предыдущие перестановки
            for position_open in range(len(permutation) + 1):
                # перебираем места для открывающей скобки
                permutation1 = permutation[:position_open] + '(' + permutation[position_open:]
                for position_closed in range(position_open + 1, len(permutation1) + 1):
                    # перебираем мест для закрывающей скобки (только правее открывающей)
                    permutation2 = permutation1[:position_closed] + ')' + permutation1[position_closed:]
                    if not permutation2 in res:
                        # избегаем повторений
                        res.append(permutation2)
        return res
                                  
        
 
        
        
        



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
