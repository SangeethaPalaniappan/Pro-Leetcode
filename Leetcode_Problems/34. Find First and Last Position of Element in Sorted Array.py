class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1] 
        if len(nums) == 0:
            return result
        result[0] = self.search1(nums, target)
        result[1] = self.search2(nums, target)
        return result
        
    def search1(self, nums, target):
        index = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index    

    def search2(self, nums, target):
        index = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index            


