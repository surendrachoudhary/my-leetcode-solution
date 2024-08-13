class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(index, nums):
            if index == len(nums):
                return  [[]]

            result = []

            listing = helper( index +1, nums)

            for p in listing:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[index])
                    result.append(pCopy)

            return result     

        return helper(0, nums)