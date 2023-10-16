class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1    
        sums = 0
        for j in hm.values():
            result = ((j) * (j - 1)) // 2   
            sums += result 
        return sums   