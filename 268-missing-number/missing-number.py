class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_xor = 0

        #XOR with given number
        for i in nums:
            nums_xor ^= i

        #XOR with the given range
        for i in range(n+1):
            nums_xor ^= i

        #return the missing number
        return nums_xor