def twoSum(nums, target):
    secondary_list = {}
    for i in range(len(nums)):
        current = nums[i]                       
        if target - current in secondary_list.values():
            for k, v in secondary_list.items():
                if v == target - current:
                    return [k, i]
        else:
            secondary_list[i] = current
    pass

import unittest

class Tests_Solution(unittest.TestCase):
        
    def test_1(self):
        List = [-8, 15, 22, 3]
        target = 7
        Answer = twoSum(List, target)
        self.assertEqual(Answer, [0, 1])
            
    def test_2(self):
        List = [-8, 15, 22, 3]
        target = 8
        self.assertIsNone(twoSum(List, target))
        
    
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
