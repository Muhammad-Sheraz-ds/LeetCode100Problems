class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c=0
        seen = dict()
        for i in words:
            try:
                if seen[i]==1:
                    c+=1
            except:
                if self.isSubsequence(i,s):
                    c+=1
                    seen[i] = 1
                else:
                    s[i]=0
        return c
    def isSubsequence(self, s: str, t: str) -> bool:
        ls= len(s)
        lt = len(t)
        s_i=0
        t_i=0
        while True:
            if s_i==ls:
                return True
            elif lt==t_i:
                return False
            if s[s_i]==t[t_i]:
                s_i+=1
            t_i+=1