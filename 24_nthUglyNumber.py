class Solution:
    def nthUglyNumber(self, n):

        ugly=[1]
        i2 = 0
        i3 = 0
        i5 = 0
        p2=2*ugly[i2]
        p3=3*ugly[i3]
        p5=5*ugly[i5]

        while(len(ugly) < n):
            minimum = min(min(p2,p3),p5)
            ugly.append(minimum)
            if(minimum == p2):
                i2 += 1
                p2 = ugly[i2] * 2
            if(minimum == p3):
                i3 += 1
                p3 = ugly[i3] * 3
            if(minimum == p5):
                i5 += 1
                p5=ugly[i5] * 5
        return ugly[-1]

import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_threeSumClosest(self):
        enter = 2
        out =  2
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)

    def test_2_threeSumClosest(self):
        enter = 5
        out =  5
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)

    def test_3_threeSumClosest(self):
        enter = 7
        out =  8
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)

    def test_4_threeSumClosest(self):
        enter = 10
        out =  12
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)

    def test_5_threeSumClosest(self):
        enter = 1
        out =  1
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)

    def test_6_threeSumClosest(self):
        enter = 800
        out =  12754584
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)

    def test_7_threeSumClosest(self):
        enter = 1600
        out =  1399680000
        answer = Solution()
        z = answer.nthUglyNumber(enter)
        self.assertEqual(z, out)        

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
