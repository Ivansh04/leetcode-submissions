class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}
        cnt=0
        def dfs(s):
            if len(s) in memo:
                return memo[len(s)]
            if not s:
                return 1
            if s[0]=='0':
                return 0

            ans=dfs(s[1:])
            
            if (len(s)>=2 and (s[0]=='1' or (s[0]=='2' and int(s[:2])<27))):
                 ans+=dfs(s[2:])
            memo[len(s)]= ans
            return ans
        
        return dfs(s)     
        
        