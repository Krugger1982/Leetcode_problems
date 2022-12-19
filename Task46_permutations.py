class Solution:
    def permute(self, nums):
        result = []
        x = nums.pop()
        if len(nums) == 0:
            return [[x]]
        else:
            recursed_nums = self.permute(nums)
            for sublist in recursed_nums:
                for i in range(len(sublist)):
                    result.append(sublist[:i] + [x] + sublist[i:])
                result.append(sublist + [x])
            return result



import unittest

class Tests_permute(unittest.TestCase):

        
    def test_1_permute(self):
        print()
        input_array = [0, 1]
        output_array = [[0, 1], [1, 0]]
        answer = Solution()
        permuted = answer.permute(input_array)
        print(permuted)
        self.assertEqual(len(output_array), len(permuted))
        for permutation in permuted:
            self.assertTrue(permutation in output_array)

    def test_2_permute(self):
        print()
        input_array = [1]
        output_array = [[1]]
        answer = Solution()
        permuted = answer.permute(input_array)
        print(permuted)
        self.assertEqual(len(output_array), len(permuted))
        for permutation in permuted:
            self.assertTrue(permutation in output_array)

    def test_3_permute(self):
        print()
        input_array = [1, 2, 3]
        output_array = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        answer = Solution()
        permuted = answer.permute(input_array)
        print(permuted)
        self.assertEqual(len(output_array), len(permuted))
        for permutation in permuted:
            self.assertTrue(permutation in output_array)

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
