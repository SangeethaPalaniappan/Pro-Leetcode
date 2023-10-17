class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        i = 0
        # Add even numbers in the dictionary
        while i < len(nums):
            if nums[i] % 2 == 0:
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1            
            i += 1 
           
        # if the dictionary is empty return -1    
        if dic == {}:
            return -1
            
        # else find the max value and max key    
        r = max(dic.values())
        s = max(dic.keys())

        # check, the keys in the dictonary less than the max key - this case if two numbers have equal count 
        # condition will satisfy only if the value is equal  
        for j in dic.keys():# j is key 
            if j < s and dic.get(j) == r: # dic.get(j) is the value
                s = j
        return s

# 1. Ex: {2:3,4:3,6:3,8:3,10:3}        
# in this(#A) case the loop goes till 2 and return 2

# 2. Ex: {}
# since the dictonary is empty -1 will be returned

# 3. Ex: {2:6, 8:12, 6:5, 4:3}
# in this case all condition will fail and return s which is 8



