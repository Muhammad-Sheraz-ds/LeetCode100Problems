class Solution:
    def a_b_c(self,a,b,c,arr):
        if a>b:
            if c > b:
                if c>a:
                    return c,a,b,{'a':a,'b':b,'c':c}
                return a,c,b,{'a':a,'b':b,'c':c}
            return a,b,c,{'a':a,'b':b,'c':c}
        if b>a:
            if c > a:
                if c>b:
                    return c,b,a,{'c':c,'b':b,'a':a}
                return b,c,a,{'a':a,'b':b,'c':c}

            return b,a,c,{'a':a,'b':b,'c':c}
        if c>a:
            if b > a:
                if b>c:
                    return b,c,a,{'a':a,'b':b,'c':c}
                return c,b,a,{'c':c,'b':b,'a':a}
            return c,a,b,{'a':a,'b':b,'c':c}
        if a==b==c:
            return a,b,c,{'a':a,'b':b,'c':c}
        if a==b:
            if c>a:
                return c,a,b,{'a':a,'b':b,'c':c}
            return a,b,c,{'a':a,'b':b,'c':c}
        if b==c:
            if c>a:
                return b,c,a,{'a':a,'b':b,'c':c}
            return a,b,c,{'a':a,'b':b,'c':c}




    def longestDiverseString(self, a, b, c):
        d = {'a':a,'b':b,'c':c}
        prev = ''
        res = ''
        a_0 = 0
        b_0 = 0
        c_0=0
        while True:
            a, b, c, d = self.a_b_c(a, b, c, d)
            if a==b==0 or b==c==0 or c==0==a:
                break
            s=''
            if d[a]!=0:
                if d[a]>1:
                    s+='a'
                    d[a]-=1
                    a_0+=1
                s += 'a'
                d[a] -= 1
                a_0+=1
            if d[b]!=0:
                if b>1:
                    s+='b'
                    d[b]-=1
                    b_0+=1
                s += 'b'
                d[b] -= 1
                b_0+=1
            if d[c]!=0:
                if b>1:
                    s+='c'
                    d[c]-=1
                    c_0+=1
                s += d[c]
                d[c] -= 1
                c_0+=1
            if s!='' and len(res)>2:
                st = res[-2]+res[-1]
                if len(st)>3 and st[0:3]!=st[0]*3 and a_0!=b_0!=c_0:
                    res+=s
        return res


