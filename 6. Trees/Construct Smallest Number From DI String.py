class Solution:
    def smallestNumber(self, pattern):
        self.n = len(pattern)
        self.count_val = [0]*n

        self.res = ''
        if pattern[0]=='I':
            self.count_val(pattern)
        else:
            self.count_val(pattern)

    def string_i(self,pattern):
        if self.d==0:
            self.res += str(1)
            i=0
            while i < self.n:
                self.res+=str(i)
                i+=1
        else:
            self.res='1'
            i = 0
            while i < self.n:



                i += 1



        while True:



    def string_d(self, pattern):
        pass


    def count(self,pattern):
        self.i=0
        self.d=0
        i=0
        while i<self.n:
            val = pattern[i]
            if val=='I':
                self.i+=1
            else:
                self.d+=1
            c=0
            j=i
            while i<self.n and pattern[i]!=val:
                val = pattern[i]
                i+=1
                c+=1
                if val == 'I':
                    self.i += 1
                else:
                    self.d += 1
            self.count_val[j]=c