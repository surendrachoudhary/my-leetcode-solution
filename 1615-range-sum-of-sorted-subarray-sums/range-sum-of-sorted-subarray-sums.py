class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sum = []
        for start_index in range(len(nums)):
            total = 0
            for num in range(start_index, len(nums)):
                total += nums[num]
                subarray_sum.append(total)
            
        result = 0
        subarray_sum.sort()

        for value in range(left-1, right):
            result += subarray_sum[value]

        return (result) % (10**9 + 7)

                
