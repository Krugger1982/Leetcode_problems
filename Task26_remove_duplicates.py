class Solution:
    def removeDuplicates(self, nums):
        i = len(nums)
        if i < 2:
            return len(nums)
        while i > 1:
            i -= 1
            if nums[i] == nums[i-1]:
                nums.pop(i)             
        return len(nums)

        
import unittest

class MyTests(unittest.TestCase):
    def test_1(self):
        nums = [1,1,2]
        out = [1,2]
        answer = Solution()
        k = answer.removeDuplicates(nums)
        self.assertEqual(2, k)
        self.assertEqual(nums,out)

    def test_2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        out = [0, 1, 2, 3, 4]
        answer = Solution()
        k = answer.removeDuplicates(nums)
        self.assertEqual(5, k)
        self.assertEqual(nums,out)

    def test_3(self):
        nums = [1]
        out = [1]
        answer = Solution()
        k = answer.removeDuplicates(nums)
        self.assertEqual(1, k)
        self.assertEqual(nums,out)

    def test_4(self):
        nums = [1, 1]
        out = [1]
        answer = Solution()
        k = answer.removeDuplicates(nums)
        self.assertEqual(1, k)
        self.assertEqual(nums,out)
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
