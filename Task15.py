


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()                     #Sort the array so that we can avoid redundant elements
        
        for i, n in enumerate(nums):
            print(i, n)
            if i>0 and n == nums[i - 1]:    #Find first element | avoid repetition
                continue
                
            l, r = i+1, len(nums) - 1       #For rest of array, maintain left pointer and right pointer as array is sorted
            
            while l<r:
                s = n + nums[l] + nums[r]       #Possible 3sum
                if s > 0:                       #If it is more than 0, then slide the window from right so that sum decreases (Array is sorted)
                    r -= 1
                elif s < 0:                     #If it is less than 0, then slide th window from left so that the sum increases.
                    l += 1                      
                else:
                    res.append([n,nums[l],nums[r]])     #If it is equal to 0, add it to result set
                    l += 1                              #Increase left pointer by 1. Note: We need not decrease right window as it will automatically decrease upon condition check of s>0
                    while nums[l] == nums[l-1] and l<r:
                        l += 1                  #Slide continuosly till left pointer value is same as previous. Note: Right pointer will correspondingly shift left-ward
        return res

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1_threeSum(self):
        enter =[-1,0,1,2,-1,-4]  
        out =  [[-1, -1, 2], [-1, 0, 1]]
        answer = Solution()
        z = answer.threeSum(enter)
        self.assertEqual(answer.threeSum(enter), out)
        
    def test_3_threeSum(self):
        enter =[0, 0, 0]  
        out =  [[0, 0, 0]]
        answer = Solution()
        z = answer.threeSum(enter)
        self.assertEqual(answer.threeSum(enter), out)
        
    def test_4_threeSum(self):
        enter =[ 0]  
        out =  []
        answer = Solution()
        z = answer.threeSum(enter)
        self.assertEqual(answer.threeSum(enter), out)        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
