class Solution:
    def solveEquation(self, equation):
        n=len(equation)
        i=0
        left_x = 0
        right_x = 0
        left = 0
        right = 0
        while i < n and equation[i]!='=':
            if equation[i]=='x':
                if i == 0:
                    left_x+=1
                if i != 0:
                    if equation[i]=='-':
                        left_x-=1
                    else:
                        left_x += 1
            else:
                val = ''
                while i < n and equation[i] not in ('x','+',"-"):
                    if i == 0:
                        left+=equation[i]
                    if i != 0:
                        if equation[i]=='-':
                            left_x-=1
                        else:
                            left_x += 1


