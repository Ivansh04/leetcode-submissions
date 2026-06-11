class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m=n
        res=[]
        st=''
        def dfs(n,m):
            nonlocal st
            if n==0 and m == 0:
                res.append(st[:])
                return
            if n!=0:
                st+='('
                dfs(n-1,m)
                st=st[:-1]
            if m!=0 and m>n:
                st+=')'
                dfs(n,m-1)
                st=st[:-1]
        dfs(n,m)
        return res
            
        