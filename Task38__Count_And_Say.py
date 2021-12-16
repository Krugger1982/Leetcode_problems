class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        res = '1'
        for i in range(n-1):
            res = countAndSay_recursive(res)
        return res
    
def countAndSay_recursive(Number):
    i = 0
    count = 1
    digit = Number[0]
    res = []
    while i < len(Number) - 1:
        if Number[i+1] == digit:
            count += 1
        else:
            res+=[str(count), str(digit)]
            digit = Number[i+1]
            count = 1
        i += 1
    res += [str(count), str(digit)]
    return ''.join(res)

        
import unittest

class Tests_searchInsert(unittest.TestCase):

        
    def test_1_count_and_say_1(self):
        n = 1
        ansver = Solution()
        self.assertEqual(ansver.countAndSay(n), "1")

    def test_2_count_and_say_1(self):
        n = 2
        ansver = Solution()
        self.assertEqual(ansver.countAndSay(n),"11")
        
    def test_3_count_and_say_1(self):
        n = 3
        ansver = Solution()
        self.assertEqual(ansver.countAndSay(n), "21")

    def test_4_count_and_say_1(self):
        n = 4
        ansver = Solution()
        self.assertEqual(ansver.countAndSay(n), "1211")

    def test_5_count_and_say_1(self):
        n = 5
        ansver = Solution()
        self.assertEqual(ansver.countAndSay(n), "111221")

    def test_6_count_and_say_1(self):
        n = 6
        ansver = Solution()
        self.assertEqual(ansver.countAndSay(n), "312211")        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
