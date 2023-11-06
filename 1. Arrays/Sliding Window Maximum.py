class Solution:
    def get_max(self, array,index,end):
        max = index
        max_val = array[index]
        for i in range(index,end):
            if array[i] >= max_val:
                max_val = array[i]
                max = i

        return max

    def maxSlidingWindow(self, nums, k):
        if k < 2:
            return nums
        ans = []
        n = len(nums)
        maxi = self.get_max(nums,0,k)
        ans.append(nums[maxi])
        i = k
        j = 0
        while i < n:
            if j == maxi:
                if nums[i] >= nums[maxi]:
                    maxi = i
                else:
                    maxi = self.get_max(nums,j + 1,i + 1)
            if nums[i] >= nums[maxi]:
                maxi = i
            j += 1
            i += 1
            ans.append(nums[maxi])

        return ans

