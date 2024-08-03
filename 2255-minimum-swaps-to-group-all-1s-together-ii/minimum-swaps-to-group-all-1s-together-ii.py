class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        l = 0
        window_one = max_window_one = 0
        
        for r in range(2 * n):
            if nums[r % n]:
                window_one += 1
            
            if r -l + 1 > ones:
                window_one -= nums[l % n]
                l += 1

            max_window_one = max(window_one,max_window_one)

        return ones - max_window_one

            