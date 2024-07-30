class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = 0

        for i in s:
            if i == "a":
                a_count_right += 1

        b_count_left = 0
        res = len(s)

        for i in s:
            if i == "a":
                a_count_right -= 1
            
            res = min(res, a_count_right + b_count_left)

            if i == "b":
                b_count_left += 1

        return res 