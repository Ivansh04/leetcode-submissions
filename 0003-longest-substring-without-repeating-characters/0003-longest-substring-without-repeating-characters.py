class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        l,r=0,0
        ans=0
        while l<=r and r<len(s):
            if s[r] not in se:
                se.add(s[r])
                r+=1
            else:
                se.remove(s[l])
                l+=1
            ans=max(ans,len(se))
        return ans
      

        