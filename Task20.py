class Solution:
    def isValid(self, s):
        Stack_List = []
        Open_Brackets = ['(', '{', '[']
        Close_Brackets = [')', '}', ']']
        for i in range(len(s)):
            if s[i] in Open_Brackets:
                Stack_List.append(s[i])
            else:
                # Проверка что массив не пуст и проверка соответствия скобок
                if len(Stack_List) == 0 or Close_Brackets.index(s[i]) != Open_Brackets.index(Stack_List[-1]):
                    return False
                Stack_List.pop()
        return len(Stack_List) == 0
        
        
        



import unittest
        
class Tests_Solution(unittest.TestCase):
        


    def test_1_isValid(self):
        enter = '((()))'
        out =  True
        answer = Solution()
        self.assertEqual(answer.isValid(enter), out)

    def test_2_isValid(self):
        enter = '(){}[]'
        out =  True
        answer = Solution()
        self.assertEqual(answer.isValid(enter), out)

    def test_3_isValid(self):
        enter = '(]'
        out =  False
        answer = Solution()
        self.assertEqual(answer.isValid(enter), out)

    def test_4_isValid(self):
        enter = '({[]})'
        out =  True
        answer = Solution()
        self.assertEqual(answer.isValid(enter), out)

    def test_5_isValid(self):
        enter = '([())]'
        out =  False
        answer = Solution()
        self.assertEqual(answer.isValid(enter), out)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
