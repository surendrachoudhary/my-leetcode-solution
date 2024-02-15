class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        value = 0

        for i in range(n+1):
            value += i

        return value - total 