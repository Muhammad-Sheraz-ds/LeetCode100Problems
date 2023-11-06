class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in s:
            try:
                d[i]+=1
            except:
                d[i]=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
