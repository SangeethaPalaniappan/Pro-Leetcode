class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        arr = []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for d in dic.keys():
            m = dic.get(d)
            if m > n:
                return d
        