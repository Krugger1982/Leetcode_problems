class Solution:
    def firstMissingPositive(self, nums):
        set_nums = set(nums)
        i = 1        
        while i < len(nums) + 1:
            if i not in set_nums:
                return i
            i += 1
        return i
        
        

        
import unittest

class Tests_firstMissingPositive(unittest.TestCase):

        
    def test_1_firstMissingPositive(self):
        nums = [1,2,0]
        ansver = Solution()
        self.assertEqual(ansver.firstMissingPositive(nums), 3)

    def test_2_firstMissingPositive(self):
        nums = [3,4,-1,1]
        ansver = Solution()
        self.assertEqual(ansver.firstMissingPositive(nums), 2)

    def test_3_firstMissingPositive(self):
        nums = [7,8,9,11,12]
        ansver = Solution()
        self.assertEqual(ansver.firstMissingPositive(nums), 1)

    def test_4_firstMissingPositive(self):
        nums = [1]
        ansver = Solution()
        self.assertEqual(ansver.firstMissingPositive(nums), 2)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
