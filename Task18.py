class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for a in range(len(nums) - 3):
            for d in range(len(nums) - 1, a + 2, -1):
                b = a + 1
                c = d - 1
                

                while b < c:
                    if nums[a] + nums[b] + nums[c] + nums[d] < target:
                        b += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        c -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c -= 1
                        b += 1
                        while b < c and nums [b] == nums[b-1]:
                            b += 1
                        while b < c and nums [c] == nums[c+1]:
                            c -= 1
                            
        # избавимся от повторов
        for i in range(len(res) - 1, 0, -1):
            if res[i] in res[:i]:
                res.pop(i)

        return res






import unittest
        
class Tests_Solution(unittest.TestCase):
        
    def test_1_fourSums(self):
        enter = [1,0,-1,0,-2,2]
        target = 0
        out =  [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        answer = Solution()
        z = answer.fourSum(enter, target)
        self.assertEqual(z, out)


    def test_2_fourSums(self):
        enter = [-3,-1,0,2,4,5]
        target = 0
        out = [[-3,-1,0,4]]
        answer = Solution()
        z = answer.fourSum(enter, target)
        self.assertEqual(z, out)


if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
