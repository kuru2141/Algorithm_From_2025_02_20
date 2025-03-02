import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    sen = input()
    a = 0
    b = 0
    
    for i in range(len(sen)):
        if sen[i] == '(':
            a += 1
        elif sen[i] == ')':
            b += 1
            if a == 0:
                break

        if a == b:
            a = 0
            b = 0

    if a == 0 and b == 0:
        print('YES')
    else:
        print('NO')