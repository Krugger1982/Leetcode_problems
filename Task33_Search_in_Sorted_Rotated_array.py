class Solution:
    def search(self, nums, target, left=0, right=-1):
        if len(nums) == 0:
            return -1
        if right == -1:
            right = len(nums) - 1
            # определим правую границу списка (ее индекс)
        middle = (left + right) // 2
        
        if nums[middle] == target:
            return middle
        if nums[left] < nums[middle]:
            if nums[left] <= target and target < nums[middle]:
            # левая половина списка - не провернутая и target подходит для поиска в ней
                return binary_search(nums, target, left, middle-1)
            else:
            # левая половина списка - не провернутая и target лежит за пределами этой части списка
                return self.search(nums, target, middle+1, right)    # тогда надо искать в правой части
        else:
            # если левая половина провернута, тогда не провернута правая половина
            if middle < right and nums[middle+1] <= target and target <= nums[right]:
                # если target дежит в пределах границ правой половины списка
                return binary_search(nums, target, middle+1, right)
            elif left < middle:
                # a если target дежит не в пределах границ правой половины списка,
                # тогда искать нужно в левой половине - при условии что левая половина - не 
                return self.search(nums, target, left, middle-1)
        return -1
                
                
            
        

def binary_search(nums, target, left=0, right=-1):
    if len(nums) == 0:
        return -1
    if right == -1:
        right = len(nums) - 1
    middle = left + (right - left) // 2
    if nums[middle] == target:
        return middle
    elif nums[middle] > target and middle > left:
        return binary_search(nums,target, left, middle-1)
    elif nums[middle] < target and middle < right:
        return binary_search(nums, target, middle+1, right)
    return -1
    


import unittest
        
class Tests_Solution(unittest.TestCase):
        

    def test_1_binary_search(self):
        enter = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 4
        out = 4
        answer = binary_search(enter, target)
        
        self.assertEqual(answer, out)

    def test_2_binary_search(self):
        enter = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 9
        out = -1
        answer = binary_search(enter, target)
        self.assertEqual(answer, out)
        
    def test_3_binary_search(self):
        enter = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 8
        out = 8
        answer = binary_search(enter, target)

    def test_4_binary_search(self):
        enter = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        target = 0
        out = 0
        answer = binary_search(enter, target)        
        self.assertEqual(answer, out)

    def test_1_search(self):
        enter = [6, 7, 8, 0, 1, 2, 3, 4, 5]
        target = 4
        out = 7
        answer = Solution()
        z = answer.search(enter, target)
        
        self.assertEqual(z, out)        

    def test_2_search(self):
        enter = [6, 7, 8, 0, 1, 2, 3, 4, 5]
        target = 6
        out = 0
        answer = Solution()
        z = answer.search(enter, target)
        
        self.assertEqual(z, out)    

    def test_3_search(self):
        enter = [1]
        target = 6
        out = -1
        answer = Solution()
        z = answer.search(enter, target)
        
        self.assertEqual(z, out)

    def test_5_search(self):
        enter = [6]
        target = 1
        out = -1
        answer = Solution()
        z = answer.search(enter, target)
        
        self.assertEqual(z, out)        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
