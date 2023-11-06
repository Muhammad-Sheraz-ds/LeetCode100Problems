class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        dp = {0: -1}
        arr1.sort()
        j = 0

        for a in arr1:
            temp = {}
            for key in dp:
                if a > dp[key]:
                    temp[a] = min(temp.get(a, float('inf')), key)
                while j < len(arr2) and arr2[j] <= dp[key]:
                    j += 1
                if j < len(arr2):
                    temp[arr2[j]] = min(temp.get(arr2[j], float('inf')), key + 1)
            dp = temp

        if dp:
            return min(dp.values())
        return -1


# Test
solution = Solution()
arr1 = [0, 11, 6, 1, 4, 3]
arr2 = [5, 4, 11, 10, 1, 0]
result = solution.makeArrayIncreasing(arr1, arr2)
print(result)  # Output should be 5


class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        m = max(arr1)
        m2 = max(arr2)
        m = max(m,m2)
        dp =[False]*(m+1)
        steps=0
        n1 = len(arr1)
        n2 = len(arr2)
        for i in arr2:
            dp[i] = True
        i = 0
        while i < n1:
            if i-1>=0 and i+1<n1 and arr1[i-1]==arr1[i+1]:

                return -1
            if arr1[i] <= arr2[]
            if i - 1 >= 0 and arr1[i - 1] == arr1[i]:
                if i+1==n1:
                    e = arr1[i - 1]
                elif i+1 < n1  and (arr1[i+1] <arr1[i] or abs(arr1[i] - arr1[i+1])<=1):
                    return -1
                else:
                    s = arr1[i - 1] + 1
                s = arr1[i - 1] + 1
                e = arr1[i + 1]
                stop = True
                for k in range(s, e):
                    if dp[k]:
                        arr1[i] = k
                        stop = False
                        break
                if stop:
                    return -1
                steps+=1
            if i + 1 < n1 and arr1[i] > arr1[i+1]:
                if i==0:
                    s = 1
                else:
                    s = arr1[i-1]+1
                e = arr1[i+1]+1
                stop = True
                for k in range(s,e):
                    if dp[k]:
                        arr1[i]=k
                        stop=False
                        break
                if stop:
                    return  -1
                steps+=1
            i+=1
        return steps




'''
def find_upper_bound(self, arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
def find_lower_bound(self, arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            left = mid + 1
        else:
            right = mid
    return left
    '''