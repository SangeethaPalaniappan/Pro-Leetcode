class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500, "CM":900,"M":1000}    
        f=0
        c=0
        while c!=(len(s)-1) and c<(len(s)-1):
            h=s[c]+s[c+1]
            if h in d.keys():
                f+=d.get(h)
                c=c+2
            else:
                f+=d.get(s[c])  
                c+=1 
        if c<=len(s)-1:
            e=d.get(s[len(s)-1])
            f=f+e
        return f

           
        