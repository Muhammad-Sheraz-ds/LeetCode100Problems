class Solution:
    def findTheDifference(self, s, t):
        d = dict()
        for i in t:
            try:
                d[i]+=1
            except:
                d[i]=1
        c = dict()
        for i in s:
            try:
                c[i]+=1
            except:
                c[i]=1

        i=0
        while i < len(t):
            try:
                if d[t[i]]>c[t[i]]:
                    return t[i]
            except:
                return t[i]
            i+=1




            i+=1

