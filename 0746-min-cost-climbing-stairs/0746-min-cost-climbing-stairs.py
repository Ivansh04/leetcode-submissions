class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        memo={0:0,1:0}
        def dfs(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]=min(dfs(n-1)+cost[n-1],dfs(n-2)+cost[n-2])
                return memo[n]
        return dfs(n)