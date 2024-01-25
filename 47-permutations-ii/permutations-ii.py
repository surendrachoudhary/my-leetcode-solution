from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(index, nums):
            if index == len(nums):
                if nums not in ans:
                    ans.append(nums.copy())
                return 
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1, nums)
                nums[index], nums[i] = nums[i], nums[index]

        backtrack(0, nums)
        return ans
