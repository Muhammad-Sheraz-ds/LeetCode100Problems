class Solution:
    def minSubArrayLen(self, target,nums):
        n = len(nums)
        sum_array = []
        start=0
        i=0
        cont = True
        start = 0
        while i < n:
            if target<sum_array:
                while True:
                    if sum_array[i]-sum_array[start]>target:
                        start+=1
                    else:
                        max = min(m,i-start)
                        cont = False
                        break
        start=0
        m = 0
        sum =0
        while i < n:
            sum+=sum_array[i]

