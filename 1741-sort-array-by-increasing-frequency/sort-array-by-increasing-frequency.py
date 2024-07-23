class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = collections.defaultdict(int)

        for number in nums:
            dic[number] += 1

        sorted_nums = sorted(nums, key=lambda x: (dic[x], -x))

        return sorted_nums
