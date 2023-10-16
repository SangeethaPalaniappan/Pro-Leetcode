class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums) // 3
        sets = set(nums)
        for i in sets:
            if nums.count(i) > n:
                arr.append(i)
        return arr        
