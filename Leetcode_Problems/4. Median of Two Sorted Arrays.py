class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = y = k = 0

        arr = [0] * (len(nums1) + len(nums2))

        while x < len(nums1) and y < len(nums2):
            if nums1[x] >= nums2[y]:
                arr[k] = nums2[y]
                k += 1
                y += 1
            elif nums1[x] < nums2[y]:
                arr[k] = nums1[x]   
                k += 1
                x += 1
        while y < len(nums2):
            arr[k] = nums2[y]
            y += 1
            k += 1
        while x < len(nums1):
            arr[k] = nums1[x]
            x += 1    
            k += 1
        n = (len(arr) - 1 )// 2   
        
        if len(arr) % 2 == 0:
            m = arr[n] + arr[n + 1]
            median = m / 2
        else:
            median = arr[n]
        return median       