
class Solution:
    def dp(self, i, nums, dct):
        if i >= len(nums):
            return False
        if i == len(nums)-1:
            return True
        if i in dct:
            return dct[i]
        x = False
        for j in range(1, nums[i]+1):
            x = x or self.dp(i+j, nums, dct)
        dct[i] = x
        return x

    def canJump(self, nums):
        n = len(nums)
        tr = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= tr:
                tr = i
        return tr == 0
