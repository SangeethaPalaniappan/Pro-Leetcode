# 1952. Three Divisors
class Solution:
    def isThree(self, n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count == 3:
            return 1
        return 0            