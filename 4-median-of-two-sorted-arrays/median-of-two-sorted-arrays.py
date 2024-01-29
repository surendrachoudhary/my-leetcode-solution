class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        first = 0
        second = 0
        merged_array = []

        while first< n1 and second < n2:
            if nums1[first] <= nums2[second]:
                merged_array.append(nums1[first])
                first += 1
            else:
                merged_array.append(nums2[second])
                second += 1
        
        while first < n1:
            merged_array.append(nums1[first])
            first += 1

        while second < n2:
            merged_array.append(nums2[second])
            second += 1
    
        
        result = 0

        if len(merged_array) % 2 == 0:
            mid = len(merged_array)//2 -1
            mid_1 = (len(merged_array)//2 + 1) -1
            result = (merged_array[mid] + merged_array[mid_1])/2
        else:
            result = merged_array[len(merged_array)//2]
        return result