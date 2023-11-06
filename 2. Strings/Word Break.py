class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i=0
        list =''
        n = len(wordDict)
        while i < n:
            list+=wordDict[i]
            i+=1
        si=0
        j=0
        sl=len(s)
        li=0
        ll = len(list)
        if sl <= ll:
            while True:
                if si==sl:
                    return True
                if ll==li:
                    return False
                if s[si]==list[li]:
                    si+=1
                li+=1



        else:
            si=0
            li=0
            nn=len(s)
            n=len(list)
            while si < nn:
                if list[li]!=s[si]:
                    return False
                si+=1
                li=(li+1)%n
            return True






