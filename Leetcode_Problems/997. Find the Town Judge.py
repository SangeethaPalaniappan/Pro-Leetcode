# 997. Find the Town Judge

class Solution:
    def findJudge(self, n, trust):
        length = len(trust)

        dic = {}
        for i in range(1, n + 1):
            dic[i] = 0
        for bond in trust:
            dic[bond[0]] += 1

        judge = -1

        for key in dic.keys():
            if dic[key] == 0:
                judge = key

        if judge != -1:
            for arr in trust:
                if arr[1] == judge:
                    dic[arr[0]] = -1
            count = 0        

            for key in dic.keys():
                if key != judge:
                    if dic[key] == -1:
                        count += 1
                    else:
                        return -1    
        return judge
                