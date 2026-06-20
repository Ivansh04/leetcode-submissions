class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r=len(heights)
        c=len(heights[0])
        res=[]
        p=a=False
        def dfs(i,j,prev):
            nonlocal a,p
            if(i<0 or i>=r or j<0 or j>=c or heights[i][j]>prev or 
            (i,j) in visited):
                return
            visited.add((i,j))
            if(i==0 or j==0):
                p=True
            if(i==r-1 or j==c-1):
                a=True
            
            if a and p:
                return True
            if(dfs(i+1,j,heights[i][j]) or
            dfs(i,j+1,heights[i][j]) or
            dfs(i-1,j,heights[i][j]) or
            dfs(i,j-1,heights[i][j])):
               return True
            return False



        for i in range(r):
            for j in range(c):
                visited=set()
                if dfs(i,j,float('inf')):
                    res.append([i,j])
                p=a=False
        return res