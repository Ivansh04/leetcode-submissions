class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        ar=[0]*n
        ar[0]=nums[0]
        ar[1]=max(nums[0],nums[1])
        for i in range(2,n):
            ar[i]=max(ar[i-1],ar[i-2]+nums[i])

        return ar[n-1]