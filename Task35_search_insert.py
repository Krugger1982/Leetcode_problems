##Given a sorted array of distinct integers and a target value, return the index if the target is found.
##If not, return the index where it would be if it were inserted in order.
##You must write an algorithm with O(log n) runtime complexity.

# Решение будет закблючаться в двоичном поиске. Фабула такая:
# Вачале отсечем target?который назодится за пределами списка (меньше минимальнго или больше максимального)
# Делим массив примерно пополам. mid - середина. Если nums[mid] является искомым элементом - возвращаем мид
# Если искомое число меньше - ищем левее чем мид, искомое число больше - ищем правее.
# Если массив в котором ищем сжимается до одного элемента и этот элемент не является искомым (элемент не найден, надо вставлять), тогда проверяем условия:
# target больше этого элемента - возвращаем right + 1
# target меньше  этого элемента - возвращаем left - 1 
# крайние случае, помним, мы отсекли в самом начале, так что target ОБЯЗАТЕЛЬНО должен быть ВНУТРИ списка, то есть результат лежит в множестве [1, len(nums) - 1]

class Solution:
    def searchInsert(self, nums, target):
        # сначала отсечем крайние случае - когда target лежит за пределами списка
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # далее реализуем рекурсивный двоичный поиск
        right = len(nums) - 1
        return self.search_recursive(nums, target, 0, right)

    def search_recursive(self, nums, target, left, right):
        if left == right:
        # поиск в единичном списке
            if target <= nums[left]:
                return left
            else:
                return right + 1
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid          # если результат найден
        if target < nums[mid] and left == mid:
            # если в рассматриваемом фрагменте 1 или 2 элемента, то mid занимает место левой границы
            return left
            # вставляем вместо левой границы, весь кусок сдвигается вправо на 1   
        if target < nums[mid]:
            # если в рассматриваемом куске  3 или больше элементов - ищем левее mid
            return self.search_recursive(nums, target, left, mid - 1)
        if target > nums[mid]:
            # ищем правее mid
            return self.search_recursive(nums, target, mid+1, right)
        
        
import unittest

class Tests_searchInsert(unittest.TestCase):
        
    def test_1_less_min(self):
        nums = [0, 1]
        target = 5
        out = 2
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)
        
    def test_2_more_max(self):
        nums = [1, 2]
        target = 0
        out = 0
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)

    def test_3_found_on_right_board(self):
        nums = [1, 2, 3]
        target = 3
        out = 2
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)

    def test_4_found_on_left_board(self):
        nums = [1, 2, 3]
        target = 1
        out = 0
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)    

    def test_5_insert_inside(self):
        nums = [1, 2, 5]
        target = 4
        out = 2
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)  

    def test_6_insert_inside(self):
        nums = [1, 4, 5]
        target = 3
        out = 1
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)

    def test_6_from_leetcode(self):
        nums = [3,5,7,9,10]
        target = 8
        out = 3
        
        Answer = Solution()
        self.assertEqual(Answer.searchInsert(nums, target), out)         

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
