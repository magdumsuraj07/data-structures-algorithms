class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        originalN = n

        # If n is -ve; make it +ve
        if n < 0:
            n = n * -1

        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n // 2
            else:
                ans = ans * x
                n = n - 1

        if originalN < 0:
            ans = 1 / ans

        return ans
