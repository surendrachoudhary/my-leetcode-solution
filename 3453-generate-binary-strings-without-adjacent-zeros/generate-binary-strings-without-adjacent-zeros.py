class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        def helper(i, string):
            if len(string) >= n:
                ans.append(string)
                return 
            
            for j in "01":
                if string and string[-1] == "0" and j == "0":
                    continue 
                helper(i+1, string + j)

        helper(0, "")
        return ans 
                
