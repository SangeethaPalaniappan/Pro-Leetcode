class Solution:
    def integerBreak(self, n: int) -> int:
        # need to separathe the n into k whose sums(k) = n and find the greatest mul(k)
        if n == 2 or n== 3:
            return n - 1
        if n == 4:
            return n
        reminder = n % 3
        div = n // 3
        if reminder == 0:
            result = 3 ** div
        elif reminder == 1:
            result = (3 ** (div - 1)) * 4     
        elif reminder == 2:
            result = (3 ** div) * 2 
        return result