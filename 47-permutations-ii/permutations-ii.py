class Solution:
    def permuteUnique(self, nums):
        def helper(pos, n, nums, ans):
            # Base Case executes when we have traversed the entire nums[]
            if pos >= n:
                ans.append(nums.copy())
                return

            # Set ensures we are not taking duplicates and thus not making Duplicate Permutations
            unique_set = set()

            # The rest logic remains exactly the same
            for i in range(pos, n):
                # If we have encountered the element before, we will simply skip the rest of iterations
                if nums[i] in unique_set:
                    continue

                # We insert nums[i] so that we don't create Duplicate Permutations
                unique_set.add(nums[i])

                # We simply use our swapping logic to create Permutations
                nums[pos], nums[i] = nums[i], nums[pos]

                # Ask recursion to do the rest of the task
                helper(pos + 1, n, nums, ans)

                # Backtrack and undo the change we have done
                nums[pos], nums[i] = nums[i], nums[pos]

        ans = []
        helper(0, len(nums), nums, ans)
        return ans
