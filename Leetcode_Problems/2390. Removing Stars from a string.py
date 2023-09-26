class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        k = len(s)
        
        while i != k :
        
            if s[i] == "*":
                if i != 0:
                    stack.pop()
                    i += 1    
                pass    
            else:
                stack.append(s[i])
                i += 1
        string = ""
        for j in range(len(stack)):
            string += stack[j]    
        return string   

        