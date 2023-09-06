class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = s.split(" ") # Removing the space [the string will be in the list]
        s = len(i) - 1 
        while s != 0: # iterate from the end of the list
            if i[s] != "": # if there is no space then return the length of that word
                d = len(i[s])
                return d
            s -= 1
        return len(i[s])
