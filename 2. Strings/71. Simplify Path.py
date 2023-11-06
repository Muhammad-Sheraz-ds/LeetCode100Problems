class Solution:
    def simplifyPath(self, path):
        ans = '/'
        i = 0
        n = len(path)
        while i < n-1:
            if path[i]=='/':
                if ans[-1] != '/':
                    ans+='/'
                while i< n-1 and path[i]=='/':
                    i+=1
            elif path[i]=='.':
                if i+2 < n-1 and path[i:i+3]=='...':
                    ans+='/'
                    while i < n-1:
                        ans+=path[i]
                        i+=1

                else:
                    i+=2
            else:
                ans+=path[i]
                i+=1
        return ans