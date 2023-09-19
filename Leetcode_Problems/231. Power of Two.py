class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = n
        if n == 0 or n == 1:
            return n
        count = 0
        if n > 0:
            while n % 2 == 0:
                count += 1
                n = n // 2
            k = 2 ** count
            if k == m:
                return 1
            else:
                return 0       