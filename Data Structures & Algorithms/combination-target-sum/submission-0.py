class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        l=len(nums)
        sum=0
        def dsf(n,sum):
            if sum==target:
                res.append(sol[:])
                return
            elif sum>target or n==l :
                return
            sum1=sum+nums[n]
            sol.append(nums[n])
            dsf(n,sum1)
            sol.pop()
            dsf(n+1,sum)
        dsf(0,sum)
        return res
            
                 
        