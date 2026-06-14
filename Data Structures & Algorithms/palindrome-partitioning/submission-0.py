class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol=[]
        res=[]
        l=len(s)
        rest=''
        def pali(st):
            if st[::-1]==st:
                return True
            return False
        def dfs(s,sol,rest):
            if len(s)==1:
                sol.append(rest+s[0])
                b=True
                for i in sol:
                    if not pali(i):
                        b=False
                if b: res.append(sol[:])
                return
            rest=rest+s[0]
            dfs(s[1:],sol[:],rest)
            rest=rest[:-1]
            sol.append(rest+s[0])
            rest=''
            dfs(s[1:],sol[:],rest)
        dfs(s,sol,rest)
        return res
        
            



        