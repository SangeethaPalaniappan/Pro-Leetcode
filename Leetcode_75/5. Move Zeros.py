class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        c=0
        while c<len(nums):
            if nums[c]!=0:
                nums[i]=nums[c]
                i+=1
            c+=1   
            
        while i<len(nums):
            nums[i]=0
            i+=1
        '''
        last = len(nums)
        i=0
        while last!=i and last>i:
            if nums[i]==0:
                for j in range(i+1,last):
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                    
                last-=1
            elif nums[i]!=0:
                i+=1
            
            
            
'''