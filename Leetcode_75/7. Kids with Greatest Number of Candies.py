class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = 0
        for i in range(len(candies)):
            
            
            if candies[i]>l:
                l = candies[i]
            
        for j in range(len(candies)):
            p = candies[j] + extraCandies
            if p >= l:
                candies[j] = 1
            else:
                candies[j] = 0
        return candies            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #Brute Force    
        '''
        result = [None] * len(candies)
        for i in range(len(candies)):
            g = 1
            print(result)
            print("c",candies[i])
            s = candies[i]+extraCandies
            print("s:",s)
            for j in range(len(candies)):
                print(candies[j])
                if s < candies[j]:
                    print("l")
                    g = 0
                    break
            print("g:",g)
            if g == 0:
                print("O:")
                result[i] = 0
            else:
                result[i] = 1    
        s=result
        print(s)
        return s'''