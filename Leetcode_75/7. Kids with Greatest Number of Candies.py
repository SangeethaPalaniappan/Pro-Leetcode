
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        d=""
        if str1[0]!=str2[0]:
            return ""
        
        s=len(str1)
        f=len(str2)
        m=gcd(s,f)
        print(m)
        print(s)
        print(f)
        k=0
        for x in range(m,len(str1)):
            
            
            if k==len(str2):
                k=0
            if str1[x]==str2[k]:
                k+=1
            

            else:
                return ""
                     
        for x in range(m):  
            d+=str2[x]  
               
        return d
def gcd(a, b):
 
    # Everything divides 0
    if a == 0 or b==0:
        return 0
 
    # base case
    if a == b:
        return a
 
    # a is greater
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)        
        