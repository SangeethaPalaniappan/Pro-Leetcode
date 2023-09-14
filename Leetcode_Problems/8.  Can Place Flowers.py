class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        print(n)
        
        for i in range(0,len(flowerbed)):
            if n == 0:
                break
                print("K",n)
            if n > 0:    
                if flowerbed[i] == 0 and i+1 < len(flowerbed):
                    if flowerbed[i+1] == 0 and flowerbed[i-1] != 1:
                        n-=1
                        flowerbed[i] = 1
                    elif i == 0 and flowerbed[i+1] == 0 :
                        n-=1
                        flowerbed[i] = 1


                elif flowerbed[i] == 0 and i+1 == len(flowerbed):
                    if flowerbed[i-1] != 1:
                        n-=1
                        flowerbed[i] = 1

            
        print("n:",n)
        if n == 0:
            return 1
        return 0            
            
        
        
        
        '''m=3
        p=m*n
        i=flowerbed.count(0)
        j=flowerbed.count(1)
        if i >= p-1 and j < i :
            return 1
        else:
            return 0'''     