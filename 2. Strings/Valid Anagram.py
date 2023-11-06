class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ds = self.count_dict(s)
        dt = self.count_dict(t)
        for i in t:
            try:
                if ds[i] != dt[i]:
                    return False
            except:
                return False
        return True



    def count_dict(self,s):
        d = dict()
        for i in s:
            try:
                d[i]+=1
            except:
                d[i]=1
        return d
