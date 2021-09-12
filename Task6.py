class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        matrix = []
        for i in range(numRows):        
            matrix.append([])       # Создаем матрицу для ответов

        for i in range(len(s)):     # пробегаем по строке, занося каждую букву в соотв. строку
            if i % (2 * (numRows - 1)) < numRows:   # для части которая идет вниз
                N = i % (2 * (numRows - 1))
            else:                                   # для части которая идет вверх
                N = 2 * (numRows - 1) - i % (2 * (numRows - 1))
            matrix[N].append(s[i])
            
        for i in range(len(matrix)):
            matrix[i] = ''.join(matrix[i])
        return ''.join(matrix)


        
import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_Zigzag(self):
        s = 'ABCDEFGHIJK'
        N = 3
        r = 'AEIBDFHJCGK'
        answer = Solution()
        self.assertEqual(answer.convert(s, N), r)
        
    def test_2_Zigzag(self):
        s = 'ABCDEFGH'
        N = 2
        r = 'ACEGBDFH'
        answer = Solution()
        self.assertEqual(answer.convert(s, N), r)
        
    def test_3_Zigzag(self):
        s = 'ABCDEFGHIJKLMNOP'
        N = 4
        r = 'AGMBFHLNCEIKODJP'
        answer = Solution()
        self.assertEqual(answer.convert(s, N), r)
        




            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
