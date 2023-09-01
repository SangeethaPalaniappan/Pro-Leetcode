class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or len(strs)==1:
            return strs[0]
        else:
            first  = strs[0]
            second = strs[1]
            if len(first)>len(second):
                itr = len(second)
            else:
                itr=len(first)
            empty = ""
            for j in range(itr):
                if first[j]==second[j]:
                    empty = empty + first[j]
                else:
                    empty=empty
                    break
            if empty=="":
                return empty
            else:      
                for i in range(2,len(strs)):     
                    arr = strs[i]  
                    if len(arr)!=0:                       
                        if len(arr)>len(empty):
                            irt = len(empty)
                        else:
                            irt=len(arr)
                        for r in range(irt):
                            if len(arr)==1 and empty[0]==arr[0]:
                                empty = empty[0]
                            elif len(arr)==1 and empty[0]!=arr[0]:
                                return ""
                            if empty[r]==arr[r]:

                                continue
                            else:
                                if len(empty)!=1:
                                    empty = empty[0:r]
                                    break

                            empty = empty[0:r]    
                    else:
                        empty=arr
                        break
                return empty           


































