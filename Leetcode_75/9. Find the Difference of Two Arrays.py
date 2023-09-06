class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        
        max = len(nums2)
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        if len(nums1) > len(nums2) :
            max = len(nums1)
        nums(nums1 , nums2 , answer[0])    

        nums(nums2 , nums1 , answer[1]) 

        return answer            
        print(answer)    

def nums(n1,n2,answer):
    for i in range(len(n1)): # to traverse all the elements in the 1st array
        p = 1
        for j in range(len(n2)): # to traverse all the elements in the 2nd array
            if n1[i] == n2[j]: # to check whether the element in two arrays or not
                p = 0 # if an element in two array break the loop and check other elements
                break
        # after checking , i.e., two array contains same element
        # if not , append it to the answer list 
        if p == 1 :
            answer.append(n1[i])
                        