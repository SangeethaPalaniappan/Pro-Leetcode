# 278. First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        start = 0
        end = n
        val = n
        while start <= end:
            n = (start + end) // 2
            bv = isBadVersion(n)
            if bv == 0:
                start = n + 1
            else:
                end =  n -1   
                val = n

        return val