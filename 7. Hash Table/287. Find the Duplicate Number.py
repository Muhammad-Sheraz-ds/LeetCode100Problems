class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        hash = [None]*(n)
        for val in nums:
            if hash[val]!=None:
                return val
            hash[val]=val