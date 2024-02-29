class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0, len(nums)-1

        while start <= end:
            mid = (start + end) // 2

            val = nums[mid]

            if val == target:
                return mid #bcz index is need to be return 

            elif val > target:
                end = mid -1 
            
            else:
                start = mid+1

        return -1