class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lis = list(s)
        lis.sort()
        lis.append('')
        lis1 = list(t)
        lis1.sort()
        for i in range(len(lis)):
            if lis[i] != lis1[i]:
                return lis1[i]
