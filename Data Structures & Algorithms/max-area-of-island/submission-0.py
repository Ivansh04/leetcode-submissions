class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        a=0
        res=0
        def dfs(i, j):
            nonlocal a
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            else:
                a+=1
                grid[i][j] = 0
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    res=max(a,res)
                    a=0

        return res

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)