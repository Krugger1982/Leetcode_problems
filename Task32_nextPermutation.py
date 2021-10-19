class Solution:
    
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Флаг для окончания перебора массива
        changed = False
        # пойдем с конца списка.
        # сначаа найдем позицию намиеньшего "беспорядка", то есть где (i-1)й элемент меньше чем i-й
        i = len(nums)-1
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i -= 1
        current = i
        # после прохождения цикла получим массив, который от 0 до i-1 отвечает требованиям задачи, и значение i
        # в этом случае остаток списка (от i до конца) должен быть отсортирован по возрастанию, а значение (i-1)го элемента должно удовлетворять условию:
        # если Х - это nums[i-1], то новый nums[i-1] > X и является минимально возможным из остатка списка
        # если i == 0, то это значит, что весь исходный список был отсортирован по убыванию (максимальная возможная перестановка)
        # и он весь должен быть в итоге сортировн по возрастанию (минимально возможная перестановка)
        if i == 0:
            temp = nums[i:]
            temp.sort()
            for j in range(len(temp)):
                nums[j] = temp[j]
        else:
            temp = nums[i-1:]
            temp.sort()
            for j in range(len(temp)):
                if not changed and temp[j] > nums[i-1]:
                    nums[i-1] = temp[j]
                    changed = True
                else:
                    nums[current] = temp[j]
                    current += 1
                    
    def nextPermutation2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i==0: break
            if nums[i-1]<nums[i]:
                break
        if i==0:
            for i in range(len(nums)//2):
                nums[i], nums[-(i+1)] = nums[-(i+1)], nums[i]
        else:
            for j in range(i,len(nums)+1):
                if j==len(nums): break
                if nums[j]<=nums[i-1]:
                    break
            nums[j-1], nums[i-1] = nums[i-1], nums[j-1]
            n = (len(nums)-i)//2
            for j in range(i, n+i):
                nums[j], nums[-(j-i+1)] = nums[-(j-i+1)], nums[j]
        
            
            
        

        



import unittest
        
class Tests_Solution(unittest.TestCase):
        

    def test_1_nextPermutation(self):
        print()
        print('test1')
        enter = [1, 3, 2]
        out = [2, 1, 3]
        answer = Solution()
        answer.nextPermutation(enter)
        
        self.assertEqual(enter, out)

    def test_2_nextPermutation(self):
        print()
        print('test2')
        enter = [3, 2, 1]
        out = [1, 2, 3]
        answer = Solution()
        answer.nextPermutation(enter)
        self.assertEqual(enter, out)
        
    def test_3_nextPermutation(self):
        print()
        print('test3')
        enter = [1, 2, 3]
        out = [1, 3, 2]
        answer = Solution()
        answer.nextPermutation(enter)
        
        self.assertEqual(enter, out)
        
    def test_4_nextPermutation(self):
        print()
        print('test4')
        enter = [1]
        out = [1]
        answer = Solution()
        answer.nextPermutation(enter)
        
        self.assertEqual(enter, out)

    def test_11_nextPermutation2(self):
        print()
        print('test11')
        enter = [1, 3, 2]
        out = [2, 1, 3]
        answer = Solution()
        answer.nextPermutation2(enter)
        
        self.assertEqual(enter, out)

    def test_12_nextPermutation2(self):
        print()
        print('test12')
        enter = [3, 2, 1]
        out = [1, 2, 3]
        answer = Solution()
        answer.nextPermutation2(enter)
        self.assertEqual(enter, out)
        
    def test_13_nextPermutation2(self):
        print()
        print('test13')
        enter = [1, 2, 3]
        out = [1, 3, 2]
        answer = Solution()
        answer.nextPermutation2(enter)
        
        self.assertEqual(enter, out)
        
    def test_14_nextPermutation2(self):
        print()
        print('test14')
        enter = [1]
        out = [1]
        answer = Solution()
        answer.nextPermutation2(enter)
        
        self.assertEqual(enter, out)        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
