
class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_threeSumClosest(self):
        enter =[-1,2,1,-4]
        target = 1
        out =  2
        answer = Solution()
        z = answer.threeSumClosest(enter, target)
        self.assertEqual(z, out)


    def test_2_threeSumClosest(self):
        enter =[-12,-7,-5,-4]
        target = 1
        out =  -16
        answer = Solution()
        z = answer.threeSumClosest(enter, target)
        self.assertEqual(z, out)

    def test_3_threeSum(self):
        enter =[1,2,4,16, 36]
        target = 18
        out =  19
        answer = Solution()
        z = answer.threeSumClosest(enter, target)
        self.assertEqual(z, out)

    def test_4_threeSum(self):
        enter =[-43,61,-62,24,73,64,-23,94,-65,-27,24,-56,8,54,0,19,-100,-64,-53,6,-22,13,-18,55,-41,37,34,-43,0,-8,-95,76,73,21,-93,16,98,60,70,-32,30,-7,-27,-73,79,-26,41,32,41,-5,82,-14,50,-94,22,62,60,-48,51,12,-34,68,-40,-20,-20,46,46,-79,1,82,-98,41,-79,-43,-76,-25,-94,-16,-25,46,-95,-79,53,-1,-30,43,93,17,72,66,83,-89,-16,42,40,87,-46,40,22,85,-91,46,-77,19,-56,-28,8,47,-20,65,8,60,-49,-86,-74,56,30,79,97,-89,14,-90,66,-12,-57,46,-61,87,72,13,75,75,36,79,-16,84,-49,-86,76,68,-8,-65,-86,-11,55,-69,-59,34,63,59,-11,43,16,7,93,57,-55,2,38,64,3,22,-9,-22,-34,-84,90,-71,-88,64,-19,13,-8,-81,-95,-38,-9,-25,82,57,60,-26,66,21,8,65,-38,-68,-59,24,91]
        target = -231
        out =  -231
        answer = Solution()
        z = answer.threeSumClosest(enter, target)
        self.assertEqual(z, out)
        

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
