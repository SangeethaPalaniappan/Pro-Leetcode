# 2469. COnvert the Temperature

class Solution:
    def convertTemperature(self, celsius):
        arr = [0, 0]
        arr[0] = celsius + 273.15
        arr[1] = (celsius * 1.80) + 32.00
        return arr