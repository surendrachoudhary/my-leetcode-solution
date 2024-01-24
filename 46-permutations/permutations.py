from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the permutations
        ans = []

        def backtrack(index, nums):
            # If the current index reaches the end of the list, a permutation is complete
            if index == len(nums):
                # Append a copy of the current nums list to the ans list
                ans.append(nums.copy())
                return 
            
            # Iterate through elements starting from the current index
            for i in range(index, len(nums)):
                # Swap the elements at the current index (by itself)
                nums[index], nums[i] = nums[i], nums[index]
                
                # Recursively call the backtrack function for the next index
                backtrack(index + 1, nums)
                
                # Undo the swap to backtrack and try other possibilities
                nums[index], nums[i] = nums[i], nums[index]

        # Start the backtrack process from the beginning (index 0)
        backtrack(0, nums)

        # Return the list of permutations
        return ans
