class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(" ")
        print(a)
        o=len(a)
        p=""
        for i in range(len(a)):
            if a[i]!="":
                if i!=len(a)-1:
                    p+=a[i]+" "
                else:
                    p=p+a[i]
   
        P=p.split(" ")  
        h=len(P)      
        for i in range(h//2):

            
            print(P[h-1])
            P[i],P[h-1]=P[h-1],P[i]
            h-=1

        m=""
        r=len(P)
        for i in range(r):
            if P[i]!="":    
                if i==r-1:
                    m=m+P[i]
                else:
                    m=m+P[i]+" "
    
            
        return m   
        
        
        
        
'''
        s=s.strip()
        a=s.split(" ")
        r=len(a)
        m=""
        for i in range(r):
            p=a[r-1-i]
            if p!="":
                if i==r-1:
                    m=m+p
                else:
                    m=m+p+" "
            
        return m    '''