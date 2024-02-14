class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        extra_array = [0] * (n+1)

        for i in range(n):
            extra_array[nums[i]] =1
        
        for i in range(n+1):
            if extra_array[i] == 0:
                return i