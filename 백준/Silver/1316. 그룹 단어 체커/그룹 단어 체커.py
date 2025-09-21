import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    alpha = []
    check = 0

    sen = input().strip()
    alpha.append(sen[0])

    for i in range(1, len(sen)):
        if sen[i] in alpha:
            if sen[i] != sen[i - 1]:
                check = 1
                break
        else:
            alpha.append(sen[i])

    if not check:
        cnt += 1

print(cnt)