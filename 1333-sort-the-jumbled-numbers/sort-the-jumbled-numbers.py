class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        freq_arr = []
        for index, num in enumerate(nums):
            value = 0
            for digit in str(num):
                value *= 10
                value += mapping[int(digit)]

            freq_arr.append((value, index))
        
        freq_arr.sort()
        
        return [nums[val[1]]  for val in freq_arr]


        