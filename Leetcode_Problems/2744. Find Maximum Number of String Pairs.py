# 2744. Find Maximum Numberof String Pairs

class Solution:
    def maximumNumberOfStringPairs(self, words):
        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                
                if i != j:
                    if words[i] == words[j]:
                        count += 1
                    else:
                        words[i] = words[i][::-1]
                        if words[i] == words[j]:
                            count += 1    
        return count // 2                   