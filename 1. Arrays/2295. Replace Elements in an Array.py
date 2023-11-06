class Solution:
    def arrayChange(self, nums, operations):
        ind = dict()
        n = len(nums)
        for i in range(n):
            ind[nums[i]] = i
        for val in operations:
            nums[ind[val[0]]] = val[1]
            #ind[val[1]] = ind[val[0]]
        return nums

o = Solution()
nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]

print(o.arrayChange(nums,operations))



