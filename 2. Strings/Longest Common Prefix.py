class Solution:
    def min_length(self,array,n):
        m = 10000
        for i in range(n):
            l = len(array[i])
            if l<m:
                m=l
        return m

    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n==0:
            return ''
        if n==0:
            return strs[0]
        res = ""
        min_length = self.min_length(strs,n)
        if min_length==0:
            return ''
        i = 0
        while i< min_length:
            val = strs[0][i]
            j = 1
            while j< n:
                if strs[j][i]!=val:
                    return res
                j+=1
            i+=1
            res+=val
        return res