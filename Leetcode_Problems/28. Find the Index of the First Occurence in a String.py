class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        hay = list(haystack)
        if len(needle) > len(haystack):
            return -1
        lis = list(needle)
        arr = [None] * len(needle)
        for i in range(len(arr)):
            arr[i] = hay[i] 
        if len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    return i
            else:
                return -1        
        k = 0
        while k < len(haystack) :
            if k == 0:
                k += (len(needle) -1)
            else:
                k += 1
            if arr == lis:
                return (k - (len(needle) - 1)) 
    
            del arr[0]
            if k < len(haystack) - 1:
                arr.append(hay[k + 1]) 
  
        return -1
