n=str(input())
listn = [i for i in n]
listn.pop(-1)
numstr = ''

for nums in listn:
    numstr = numstr + nums

res = int(numstr) * 2

if numstr[-1] != '0':
    res + 1

print(res)