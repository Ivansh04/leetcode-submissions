class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        res=[]
        sol=[]
        def dfs(n):
            if n==l:
                res.append(sol[:])
                return
            dfs(n+1)
            sol.append(nums[n])
            dfs(n+1)
            sol.pop()
        dfs(0)
        return res
