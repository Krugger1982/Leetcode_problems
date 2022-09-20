import unittest


class Solution():
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print()
        print(nums)
        step_count = 0
        current_index = len(nums) -1
        if current_index == 0:
            return step_count        
        return self.recursed_jumps(current_index, nums, step_count)

    def recursed_jumps(self, current_index, nums, step_count):
        step_count += 1
        min_index = current_index
        for i in range(current_index-1, -1, -1):
            if nums[i] >= current_index - i:
                # проверка того, что из индекса i текущий current_index - достижим
                min_index= i
        if min_index == 0:
            return step_count
        return self.recursed_jumps(min_index, nums, step_count)

        

class Tests_jump(unittest.TestCase):
        
    def test_1_jump(self):
        Entrance = [2, 3, 3, 1, 4]
        expected = 2
        result = Solution()
        self.assertEqual(result.jump(Entrance), expected)


    def test_2_jump(self):
        Entrance = [2,3,0,1,4]
        expected = 2
        result = Solution()
        self.assertEqual(result.jump(Entrance), expected)

    def test_3_jump(self):
        Entrance = [2,3,0,1,4, 0, 0, 0, 1]
        expected = 3
        result = Solution()
        self.assertEqual(result.jump(Entrance), expected)

    def test_4_jump(self):
        Entrance = [0]
        expected = 0
        result = Solution()
        self.assertEqual(result.jump(Entrance), expected)

    def test_5_jump(self):
        Entrance = [1, 0]
        expected = 1
        result = Solution()
        self.assertEqual(result.jump(Entrance), expected)

    def test_6_jump(self):
       Entrance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
       expected = 12
       result = Solution()
       self.assertEqual(result.jump(Entrance), expected)

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
