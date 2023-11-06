class Solution:
    def give_start_end(self, n, ranges, i):
        v1 = i - ranges[i]
        v2 = i + ranges[i]
        if v1 < 0:
            v1 = 0
        if v2 > n:
            v2 = n
        return [v1, v2]

    def minTaps(self, n, ranges):
        coverd_area = [None for ji in range(n + 1)]
        min_start = n
        max_end = n
        for i in range(n + 1):
            area = self.give_start_end(n, ranges, i)
            if coverd_area[area[0]] != None and coverd_area[area[0]][1] < area[1]:
                coverd_area[area[0]][1] = area[1]
            else:
                coverd_area[area[0]] = area
        if coverd_area[0] == None:
            return -1
        min_start = 0
        max_end = coverd_area[0][1]
        tmp_start = 0
        tmp_end = coverd_area[0][1]
        c = 1
        i = 1
        while i <= n:
            if max_end == n:
                return c
            tmp_end = max_end
            while i <= max_end:
                if coverd_area[i] != None and coverd_area[i][1] > tmp_end:
                    tmp_end = coverd_area[i][1]
                i += 1
            if tmp_end == max_end:
                return -1
            c += 1
            max_end = tmp_end

        if max_end != n:
            return -1
        return c





class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        i=0
        while i < len(s):
            if k==0:
                break
            if s[i]==' ':
                k-=1
        return s[0:i]


