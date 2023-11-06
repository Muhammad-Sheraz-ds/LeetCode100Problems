class Solution:
    def firstMissingPositive(self, nums):
        d = dict()
        for val in nums:
            d[val]=True
        i=1
        while True:
            try:
                b =  d[i]
            except:
                return i
            i+=1
