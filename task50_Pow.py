class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = abs(n)

        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n //= 2
        return ans
