class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=str(x)
        
        e=len(r)-1
        m=0
        p=1
        while m!=e and m<e:
            if r[m]==r[e]:
                m+=1
                e-=1
            elif r[m]!=r[e]:
                p=0
                break
        return p