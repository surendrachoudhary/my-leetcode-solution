class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, element = 0, 0

        for val in nums:
            if count == 0 :
                count += 1
                element = val
            elif element == val:
                count += 1
            else:
                count -= 1

        return element 
