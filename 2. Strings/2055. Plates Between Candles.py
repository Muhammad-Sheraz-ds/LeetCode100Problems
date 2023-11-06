class Solution:
    def platesBetweenCandles(self, s, queries):
        next = dict()
        prev = dict()
        count = [0]*len(s)
        total = 0
        i=0
        while i < len(s):
            if s[i] == '|':
                c=0
                count[i] = total
                i+=1
                while i < len(s) and s[i]=='*':
                    count[i] = total
                    c+=1
                    i+=1
                if i==len(s) and s[-1]=='*':
                    break
                total+=c
                i-=1
            count[i] = total
            i+=1
        i=0
        next_index = 0
        while i < len(s):
            if s[i] == '|':
                next_index = count[i]
            prev[i] = next_index
            i+=1
        i=len(s)-1
        prev_index = total
        while i >= 0:
            if s[i] == '|':
                prev_index = count[i]
            next[i] = prev_index
            i -= 1
        l = []
        for i in queries:
            l.append(next[i[0]]-prev[i[1]])
        return l

s = Solution()
s.platesBetweenCandles("**|**|***|",[[2,5],[5,9]])




