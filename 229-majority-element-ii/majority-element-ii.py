from collections import Counter

class Solution:
    def majorityElement(self, nums):
        # Initialize counters for two potential majority elements
        cnt1, cnt2 = 0, 0 
        # Initialize placeholders for two potential majority elements
        elm1, elm2 = "inf", "inf"
        # Get the length of the input list
        n = len(nums)
        # Initialize an empty list to store the majority elements
        ans = []

        # Find potential majority elements
        for val in nums:
            if cnt1 == 0 and val != elm2:
                elm1 = val
                cnt1 += 1
            elif cnt2 == 0 and val != elm1:
                elm2 = val
                cnt2 += 1
            elif val == elm1:
                cnt1 += 1
            elif val == elm2:
                cnt2 += 1 
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Reset counters for re-counting
        cnt1, cnt2 = 0, 0

        # Count occurrences of potential majority elements
        for val in nums:
            if val == elm1:
                cnt1 += 1
            if val == elm2:
                cnt2 += 1

        # Calculate the minimum threshold for a majority element
        mini = n // 3 + 1
        # Check if potential majority elements meet the threshold and add them to the result list
        if cnt1 >= mini:
            ans.append(elm1)
        if cnt2 >= mini:
            ans.append(elm2)

        # Return the list of majority elements
        return ans
