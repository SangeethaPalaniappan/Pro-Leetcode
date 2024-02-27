# 191. Is Subsequence

class Solution:
    def hammingWeight(self, n):
        lis = str(n)
        num = int(lis)
        count = 0
        while num > 0:
            m = num % 2
            num //= 2
            if m == 1:
                count += 1
        return count        
        