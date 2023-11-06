class Solution:
    def searchInsert(self, nums, target):
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        return self.Binary_Search(nums,target,0,len(nums))

    def Binary_Search(self,nums,target,left,right):
        while left<=right:
            mid = (right+left)//2
            if nums[mid] ==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            if nums[mid]>target:
                right=mid
        return left




