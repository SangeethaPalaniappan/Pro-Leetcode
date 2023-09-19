class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "" # Create empty string
        for i in range(len(digits)): # Iterate the list
            s += str(digits[i]) # adding the integers as string in s[empty string]
        d = int(s) + 1 # after adding all the elements in the string convert the string into integer
        f = d 
        m = str(f) # To add the elements in the list convert the added integer into string
        k = []
        for g in range(len(m)):
            k.append(int(m[g]))
        return k