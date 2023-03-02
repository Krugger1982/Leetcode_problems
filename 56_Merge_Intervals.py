"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:
    def merge(self, intr):
        i = 0
        intr.sort()
        if len(intr) == 0:
            return []
        elif len(intr) == 1:
            return list(intr)
        else:
            while i < len(intr) - 1:
                if (intr[i][1] >= intr[i+1][0] and intr[i][1] >= intr[i+1][1]):
                    intr.append([intr[i][0], intr[i][1]])
                    intr.remove(intr[i])
                    intr.remove(intr[i])
                    intr.sort()
                elif (intr[i][1] >= intr[i+1][0]
                      and intr[i][1] < intr[i+1][1]):
                    intr.append([intr[i][0], intr[i+1][1]])
                    intr.remove(intr[i])
                    intr.remove(intr[i])
                    intr.sort()
                else:
                    i += 1
            return intr
