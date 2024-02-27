class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        ds = []

        def substr(index):
            if index == n:
                ans.append(ds.copy())
            
            for i in range(index, n):
                if ispalindrome(s, index, i):
                    ds.append(s[index:i+1])
                    substr(i+1)
                    ds.pop()

        def ispalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False 
                start += 1
                end -= 1

            return True 

        substr(0)
        return ans
