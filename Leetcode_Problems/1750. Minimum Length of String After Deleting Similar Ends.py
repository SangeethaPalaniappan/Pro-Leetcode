# 1750. Minimum Length of String After Deleting Similar Ends

class Solution:
    def minimumLength(self, s):
        start = 0
        end = len(s) - 1
        while start < end and s[start] == s[end]:
            b_char = s[start]
            while start <= end  and s[start] == b_char:
                start += 1
            while start <= end  and s[end] == b_char:
                end -= 1
 
        return (end - start) + 1 
