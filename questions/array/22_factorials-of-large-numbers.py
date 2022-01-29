class Solution:
    def multiply(self, num1, num2):
        '''
        Multiply two integers represented in the form of array and
        return result as an array
        '''
        m, n = len(num1), len(num2)
        res = [0] * (m+n)  # Array to store multiplication result
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = num1[i] * num2[j]
                _sum = mul + res[i+j+1]
                res[i+j+1] = _sum % 10
                res[i+j] += _sum//10
        
        # Remove leading zeros
        while res[0] == 0:
            res.pop(0)
        return res

    def factorial(self, N):
        res = [1]
        for i in range(2, N+1):
            res = self.multiply(res, [i])
        return res
