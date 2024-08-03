class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        maxLen = 1
        ans = 0
        n = len(colors)
        
        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1 + n) % n]:
                maxLen += 1
            else:
                maxLen = 1
            
            if maxLen >= k:
                ans += 1
                
        return ans
