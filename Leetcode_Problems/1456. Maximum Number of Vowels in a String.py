class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        add =0
        while k <= len(s):
           
            j = s[i : k]

            sums = j.count("a") + j.count("e") + j.count("i") + j.count("o") + j.count("u")
            if add < sums:
                add = sums
            k += 1
            i += 1
        return add