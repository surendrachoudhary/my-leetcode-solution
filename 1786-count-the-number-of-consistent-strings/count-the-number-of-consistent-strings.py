class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allow_word = set(allowed)

        count = 0
        for word in words:
            for i in word:
                if i not in set_allow_word:
                    count -= 1
                    break
            count += 1
        return count 