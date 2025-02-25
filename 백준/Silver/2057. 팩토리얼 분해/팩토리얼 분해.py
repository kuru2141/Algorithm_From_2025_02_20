N = int(input())
M = 0

fac = []
fac.append(1)

tmp = 1
i = 1
while tmp <= N:
    tmp *= i
    fac.append(tmp)
    i += 1

fac.reverse()
for ele in fac:
    if N >= ele:
        N -= ele
        M += 1

if N != 0 or M < 1:
    print('NO')
else:
    print('YES')