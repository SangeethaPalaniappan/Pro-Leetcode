class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        c = len(nums)
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        print(nums)        