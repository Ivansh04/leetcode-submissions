class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        ls=[]
        while r<len(nums):
            maxx=float('-inf')
            for i in range(l,r+1):
                maxx=max(maxx,nums[i])
            ls.append(maxx)
            l+=1
            r+=1
        return ls