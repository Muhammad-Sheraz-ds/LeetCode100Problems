class Solution:
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