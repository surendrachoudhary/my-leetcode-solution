class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            turn = False
            find = False 
            for j in nums2:
                if i == j:
                    turn = True 

                if turn == True and j > i and find == False:
                    find = True
                    ans.append(j)

                if find == False and j == nums2[len(nums2)-1]:
                    ans.append(-1)

        return ans
            