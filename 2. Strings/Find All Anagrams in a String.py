from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        dp = Counter(p)
        ds = Counter(s[0:lp])
        res = []
        for i in range(lp-1,ls):
            if dp==ds:
                res.append(i-lp+1)
            if ds[s[i-lp+1]]==1:
                del ds[s[i-lp+1]]
            else:
                ds[s[i-lp+1]] -= 1
            if i+1<ls:
                try:
                    ds[s[i+1]]+=1
                except:
                    ds[s[i + 1]] = 1

        return res




