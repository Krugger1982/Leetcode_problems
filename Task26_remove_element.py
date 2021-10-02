class Solution:
    def removeElement(self, nums, item):
        i = 0
        nums_len = len(nums)
        while i  < nums_len-1:
            if nums[i] == item:
                nums[i] = nums.pop()
                nums_len -= 1
            else:
                i+=1
    
        if nums and nums[-1] == item:
            nums.pop()
            
        return len(nums)    

        
import unittest

class MyTests(unittest.TestCase):

    def test_1(self):
        nums = [1,1,2]
        item = 1
        out = [2]
        answer = Solution()
        k = answer.removeElement(nums, item)
        self.assertEqual(1, k)
        for i in nums:
            self.assertEqual(nums.count(i),out.count(i))

    def test_2(self):
        nums = [2]
        item = 2
        out = []
        answer = Solution()
        k = answer.removeElement(nums, item)
        self.assertEqual(0, k)
        for i in nums:
            self.assertEqual(nums.count(i),out.count(i))

    def test_3(self):
        nums = [3,2,2,3]
        item = 3
        out = [2, 2]
        answer = Solution()
        k = answer.removeElement(nums, item)
        self.assertEqual(2, k)
        for i in nums:
            self.assertEqual(nums.count(i),out.count(i))

    def test_4(self):
        nums = [0,1,2,2,3,0,4,2]
        item = 2
        out = [0,1,4,0,3]
        answer = Solution()
        k = answer.removeElement(nums, item)
        self.assertEqual(5, k)
        for i in nums:
            self.assertEqual(nums.count(i),out.count(i))

    def test_4(self):
        nums = []
        item = 2
        out = []
        answer = Solution()
        k = answer.removeElement(nums, item)
        self.assertEqual(0, k)
        for i in nums:
            self.assertEqual(nums.count(i),out.count(i))
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
