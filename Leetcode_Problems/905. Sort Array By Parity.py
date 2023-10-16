class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while nums[i] % 2 == 0 and i < j:
                i += 1
            while nums[j] % 2 != 0 and j > i:
                j -= 1
            nums[i] , nums[j] = nums[j] , nums[i]         

        return nums
            