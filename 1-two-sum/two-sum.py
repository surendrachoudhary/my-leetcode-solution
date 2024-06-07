class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        var_dic = collections.defaultdict()

        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in var_dic:
                return [var_dic[diff], index]
            else:
                var_dic[nums[index]] = index
        
    
