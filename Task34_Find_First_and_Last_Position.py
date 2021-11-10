class Solution:
    def searchRange(self, nums, target):
        first = last = binary_search(nums, target)
        while first > 0 and nums[first - 1] == nums[first]:
            first -= 1
        while last  >= 0 and last < len(nums)-1 and nums[last + 1] == nums[last]:
            last += 1
        return[first, last]
            
    
def binary_search(nums, target, left=0, right=float('inf')):
    if right > len(nums):
        right = len(nums)
    if left == right:
        return -1       # в пустом куске списка target отсутствует
    center = (left + right) // 2
    if nums[center] == target:  # искомый индекс target
        return center
    if target < nums[center]:
        return binary_search(nums, target, left, center)
        # ищем в левой половине куска
    if target > nums[center]:
        return binary_search(nums, target, center + 1, right)
        # ищем в правой половине куска



        
import unittest

class Tests_searchRange(unittest.TestCase):
        
    def test_1(self):
        nums = [-8, 15, 22, 39]
        target = 7
        out = [-1, -1]
        
        Answer = Solution()
        z = Answer.searchRange(nums, target)
        for i in range(2):
            self.assertEqual(z[i], out[i])

    def test_2(self):
        nums = [-8, 15, 22, 39]
        target = 15
        out = [1, 1]
        
        Answer = Solution()
        z = Answer.searchRange(nums, target)
        for i in range(2):
            self.assertEqual(z[i], out[i])        

    def test_3(self):
        nums = [-8, 15, 15, 22, 39, 45, 88, 100, 100, 100]
        target = 15
        out = [1, 2]
        
        Answer = Solution()
        z = Answer.searchRange(nums, target)
        for i in range(2):
            self.assertEqual(z[i], out[i])

    def test_4(self):
        nums = [-8, 1, 1, 1, 1, 1, 1, 1, 1, 100]
        target = 1
        out = [1, 8]
        
        Answer = Solution()
        z = Answer.searchRange(nums, target)
        for i in range(2):
            self.assertEqual(z[i], out[i])

    def test_5(self):
        nums = [5,7,7,8,8,10]
        target = 8
        out = [3, 4]
        
        Answer = Solution()
        z = Answer.searchRange(nums, target)
        for i in range(2):
            self.assertEqual(z[i], out[i])

    def test_6(self):
        nums = [5,7,7,8,8,10]
        target = 100
        out = [-1, -1]
        
        Answer = Solution()
        z = Answer.searchRange(nums, target)
        for i in range(2):
            self.assertEqual(z[i], out[i])
            
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
