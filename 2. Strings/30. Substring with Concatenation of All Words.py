class Solution:
    def grnerate_dict(self,s,i,n,k,m):
        seen = dict()
        j=i+(m*k)
        if j >n:
            return seen,i
        while i < j:
            try:
                seen[s[i:i+k]]+=1
            except:
                seen[s[i:i+k]]=1
            i+=k
        return seen,i
    def findSubstring(self, s: str, words):
        self.ans = []
        self.d = dict()
        for e in words:
            try:
                self.d[e]+=1
            except:
                self.d[e]=1
        i=0
        k = len(words[0])
        self.k=k
        m = len(words)
        self.m = m
        n = len(s)
        self.n = n
        seen = dict()
        c=0
        while i < m*k:
            try:
                seen[s[i:i+k]]+=1
            except:
                seen[s[i:i+k]]=1
            c+=1
            i+=k
        while i <= n:
            if self.d==seen:
                self.ans.append(i-(k*m))
            if s[i:i + k] not in self.d:
                j=i
                while i < n and s[i:i + k] not in self.d:
                    i+=1
                seen,i = self.grnerate_dict(s,i,n,k,m)
                if seen==self.d:
                    self.ans.append(i-(k*m))
            if i==n:
                break
            try:
                seen[s[i:i + k]] += 1
            except:
                seen[s[i:i + k]] = 1
            c += 1
            seen[s[i-(k*m):i-(k*m)+k]]-=1
            if seen[s[i-(k*m):i-(k*m)+k]]==0:
                del seen[s[i-(k*m):i-(k*m)+k]]
            i+=k
        return self.ans

    def is_substring(self,s,array,i):
        n = i+(self.m*self.k)
        seen= dict()
        while i < n:
            try:
                v = self.d[s[i:i+self.k]]
                try:
                    seen[s[i:i + self.k]] += 1
                    if seen[s[i:i + self.k]]>self.d[s[i:i + self.k]]:
                        return i
                except:
                    seen[s[i:i + self.k]] = 1
            except:
                return i

            i+=self.k
        self.ans.append(i-(self.k*self.m))
        return i


'''class Solution:
    def findSubstring(self, s: str, words):
        self.ans = []
        self.d = dict()
        for e in words:
            try:
                self.d[e]+=1
            except:
                self.d[e]=1
        i=0
        k = len(words[0])
        self.k=k
        m = len(words)
        self.m = m
        n = len(s)
        self.n = n
        while i < n:
            self.is_substring(s,words,i)
            i+=k


        return self.ans

    def is_substring(self,s,array,i):
        n = i+(self.m*self.k)
        seen= dict()
        while i < n:
            try:
                v = self.d[s[i:i+self.k]]
                try:
                    seen[s[i:i + self.k]] += 1
                    if seen[s[i:i + self.k]]>self.d[s[i:i + self.k]]:
                        return i
                except:
                    seen[s[i:i + self.k]] = 1
            except:
                return i

            i+=self.k
        self.ans.append(i-(self.k*self.m))
        return i

'''