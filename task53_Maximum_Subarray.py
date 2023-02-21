"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
"""


class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        temp = 0
        for i in range(len(nums)):
            if temp < 0:
                temp = 0
            temp += nums[i]
            if temp > max_sum:
                max_sum = temp
        return max_sum
