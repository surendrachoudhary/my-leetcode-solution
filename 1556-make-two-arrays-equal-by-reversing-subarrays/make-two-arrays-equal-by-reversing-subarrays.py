class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_set = Counter(target)

        for i in arr:
            if i not in target_set or target_set[i] == 0:
                return False
            target_set[i] -= 1

        return True 