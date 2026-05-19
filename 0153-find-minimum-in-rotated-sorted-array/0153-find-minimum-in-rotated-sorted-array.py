class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn=float('inf')
        l=0
        h=len(nums)-1
        while l<=h:
                mid=(l+h) // 2
            
                minn=min(minn,nums[mid])
                if nums[l]>nums[mid]:
                    h=mid-1
                elif nums[h]<nums[mid]:
                    l=mid+1
                elif nums[l]<minn<nums[h]:
                    return nums[l]
                else: return minn
        return minn


        