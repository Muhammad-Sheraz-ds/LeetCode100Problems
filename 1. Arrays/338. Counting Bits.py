class Solution:
    def countBits(self, n):
        ans = [1]*(n+1)
        if n==0:
            return []
        ans[0]=0
        if n==1:
            return ans
        p=1
        i=3
        while i <= n:
            if (2**(p+1))-1==i:
                p+=1
                ans[i]=p
                i+=1
            else:
                ans[i]=p
            i+=1
        return ans



