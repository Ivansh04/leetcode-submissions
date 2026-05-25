class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for i in range(len(s2)):
            h={}
            l=len(s1)
            for k in s1:
              h[k]=h.get(k,0)+1
            j=i
            while j<len(s2) and s2[j] in h:
                if h[s2[j]]==0:
                    break
                else: 
                    h[s2[j]]=h.get(s2[j])-1
                    l-=1
                j+=1
            if l==0:
                return True
        return False
                

        
        