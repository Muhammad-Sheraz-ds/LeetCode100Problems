class Solution:
    def caontain(self,st,d):
        i=0
        v=100000000000
        ans=''
        s=''
        while i < len(st):
            s += st[i]
            if s in d and d[s]<v:
                ans=s
                v = d[s]
            i+=1
        return ans




    def replaceWords(self, dictionary, sentence):
        d = dict()
        for val in len(dictionary):
            d[dictionary[val]] = val
        l = list(sentence.split(' '))
        n = len(dictionary[0])
        ans = ''
        i = 0
        while i < len(l):
            v =self.caontain(l[i],d)
            if v!='':
                ans += v

            else:
                ans += l[i]
            ans += ' '
            i += 1
        return ans[0:-1]


