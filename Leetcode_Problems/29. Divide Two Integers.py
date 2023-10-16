class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div = dividend
        divise = divisor
        if dividend < divisor :
            return 0
        if dividend < 0 or divisor < 0 :
            if dividend < 0:
                dividend *= (-1)
            if divisor < 0:
                divisor *= (-1)
        count = 0        
        while dividend > 0:
            dividend -= divisor
            print(dividend)
            count += 1
            if dividend - divisor < 0:
                break
            
            print(dividend)    
        if div < 0:
            count *= (-1)
        if divise < 0:
            count *= (-1)
        return count