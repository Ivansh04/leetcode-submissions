class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        def bs(nums,low,high,target):
            if low>high:
                return -1
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return bs(nums,mid+1,high,target)
            elif nums[mid]>target:
                return bs(nums,low,mid-1,target)

        return bs(nums,low,high,target)
        
