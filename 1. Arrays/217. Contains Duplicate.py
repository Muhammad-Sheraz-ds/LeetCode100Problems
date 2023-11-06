class Solution:
    def containsDuplicate(self, nums):
        d = dict()
        for i in nums:
            try:
                d[i]+=1
                return True

            except:
                d[i] = 1
        return False