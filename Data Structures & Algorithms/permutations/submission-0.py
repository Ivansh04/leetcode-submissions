class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                perm.append(nums[i])

                backtrack(perm)

                perm.pop()
                used[i] = False

        backtrack([])
        return res