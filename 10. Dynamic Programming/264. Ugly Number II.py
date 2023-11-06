class Solution:
    def nthUglyNumber(self, n: int):
        d = dict()
        if n < 4 or n==5:
            d[n] = n
            return n
        d = {1:1,2:2,3:3,5:4}
        i=6
        count = 4
        while True:
            if i%2==0 or i%3==0 or i%5:
                count += 1
                d[i] = count

            if i//3 in d:
                count += 1
                d[i] = count
            if count==n:
                return i
            i+=1

