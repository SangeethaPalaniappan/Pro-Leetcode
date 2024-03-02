# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n):
        count = 0
        num = n
        if n <= 0:
            return 0
        m = self.isPowerThree(n, count)
        if 3 ** m == num:
            return 1
        return 0    

    def isPowerThree(self, n, count):
        if n <= 1:
            return count
        count += 1
        n = n // 3
        return self.isPowerThree(n, count)

