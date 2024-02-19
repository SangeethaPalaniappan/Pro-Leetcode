# 509. Fibonacci Number

class Solution:
    def fib(self, n):
        k = 1
        fib_1 = 0
        fib_2 = 1
        if n == 0 or n == 1:
            return n
        while k != n:
            fib = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib
            k += 1
        return fib    