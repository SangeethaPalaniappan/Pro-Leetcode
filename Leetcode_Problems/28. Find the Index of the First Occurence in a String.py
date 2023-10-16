class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for k in range(len(haystack)) :
            if haystack[k : length + k] == needle:
                return k    
        return -1

