class Solution:
    def minimumPushes(self, word: str) -> int:
        word_count = Counter(word)
        
        sorted_word_count = word_count.most_common()

        num_count = 0
        ans = 0
        for key, value in sorted_word_count:
            ans += value * (int(num_count / 8) + 1)                
            num_count += 1

        return ans 