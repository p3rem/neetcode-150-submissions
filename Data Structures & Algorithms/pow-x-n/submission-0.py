class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if x == 0:
            return 0
        if n == 0:
            return 1 
        for i in range(abs(n)):
            res *= x
        if n > 0:
            return res 
        if n < 0:
            return 1/res 