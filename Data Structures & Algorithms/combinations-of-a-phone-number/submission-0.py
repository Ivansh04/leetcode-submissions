class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={}
        d[2]='abc'
        d[3]='def'
        d[4]='ghi'
        d[5]='jkl'
        d[6]='mno'
        d[7]='pqrs'
        d[8]='tuv'
        d[9]='wxyz'
        res=[]
        sol=''
        l=len(digits)
        def dfs(n,sol):
            if n==l:
                res.append(sol)
                return
            s=d.get(int(digits[n]))
            sol+=s[0]
            dfs(n+1,sol)
            sol=sol[:-1]
            sol+=s[1]
            dfs(n+1,sol)
            sol=sol[:-1]
            sol+=s[2]
            dfs(n+1,sol)
            sol=sol[:-1]
            if len(s)==4:
                sol+=s[3]
                dfs(n+1,sol)
                sol=sol[:-1]
        dfs(0,sol)
        return res

            

        