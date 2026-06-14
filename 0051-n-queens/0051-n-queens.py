class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        d={'j':[],
           'sum':[],
           'sum2':[]}
        res=[]
        sol=[]
        s='.'*n
        def dfs(a,d,sol):
            if a==n:
                res.append(sol[:])
                return
            for i in range(n):
                if (i not in d['j'] and
                   (i+a) not in d['sum'] and
                   (a-i) not in d['sum2']):
                   d['j'].append(i)
                   d['sum'].append(i+a)
                   d['sum2'].append(a-i)
                   sol.append('.' * i + 'Q' + '.' * (n - i - 1))
                   dfs(a+1,d,sol)
                   d['j'].pop()
                   d['sum'].pop()
                   d['sum2'].pop()
                   sol.pop()
        dfs(0,d,sol)
        return res


                
            
                