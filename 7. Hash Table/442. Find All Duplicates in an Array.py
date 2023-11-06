class Solution:
    def findDuplicates(self, nums):
        seen = dict()
        ans = []
        n = len(nums)
        hash = [None]*(n+1)
        for val in nums:
            if hash[val]!=None and seen[val]==False:
                ans.append(val)
                seen[val]=True
            else:
                hash[val]=val
                seen[val]=False
        return ans