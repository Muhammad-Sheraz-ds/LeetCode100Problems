class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        i = 0
        j = 0
        while True:
            if i == n and j == m:
                return True
            if i==n:
                return True
            if j == m:
                return False
            if p[j] == '.':
                i += 1
                j += 1
            elif p[j] == '*':
                if p[j - 1] == '.'
                    if j==m-1:
                        return True
                    else:
                        while i < n and s[i]!=p[j+1]:
                            i+=1
                        if i==n:
                            return False
                    j+=1
                else:
                    tmp = p[j - 1]
                    while i < n and s[i] == tmp:
                        i += 1
                    j += 1

            else:
                if s[i] != p[j]:
                    if j + 1 < n and p[j] == '*':
                        j += 1
                    j += 1
                    i = 0

                else:
                    i += 1
                    j += 1



obj = Solution()
print(obj.isMatch('abc','a*b*c'))