class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        d = dict()
        for i in forbidden:
            d[i] = True
        start = 0
        steps = 0
        while start <= x:
            if start in d:
                break
            if start == x:
                return steps
            steps += 1
            start += a
        start -= b
        if start<0:
            start=0
        steps += 1
        while start <= x:
            if start == x:
                return steps
            start += a
            steps += 1
            if start in d:
                return -1
        return -1
