class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        for i in t:
            d[i]=d.get(i,0)+1
        l=0
        r=0
        ans=""
        count=0
        while r<len(s):
            d[s[r]]=d.get(s[r],0)-1
            if d[s[r]]>=0:
                count+=1
            while count==len(t):
                if ans=="" or r-l+1<len(ans):
                    ans=s[l:r+1]
                d[s[l]]=d.get(s[l],0)+1
                if d[s[l]]>0:
                    count-=1
                l+=1
            r+=1
        return ans