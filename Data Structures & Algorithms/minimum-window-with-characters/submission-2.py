class Solution:
    def minWindow(self, s: str, t: str) -> str:
       ans=''
       mil=float('inf')
       for i in range(len(s)):
           if s[i] in t:
               d={}
               for k in t:
                  d[k]=d.get(k,0)+1
               st=''
               le=len(t)
               
               for j in range(i,len(s)):
                   st=st+s[j]
                   if s[j] in t and d[s[j]]!=0:
                      d[s[j]]=d.get(s[j],0)-1
                      le-=1
                   if le==0:
                      if len(st)<mil:
                         mil=len(st)
                         ans=st
       return ans
                      
                      

                       
                

                