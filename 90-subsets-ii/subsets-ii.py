from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        ds = []

        def subset(idx):
            ans.append(ds.copy())
            
            for i in range(idx, n):
                # Skip duplicates at the same level of recursion
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                ds.append(nums[i])
                subset(i+1)
                ds.pop()

        subset(0)

        return ans
