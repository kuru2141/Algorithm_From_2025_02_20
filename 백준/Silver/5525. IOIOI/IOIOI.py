import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip('\n').lstrip('O')

tmp = 'I' + 'OI' * N
l = len(tmp)

cnt = 0
for i in range(M - l + 1):
    if S[i] != 'I':
        continue

    
    if S[i:i + l] == tmp:
        cnt += 1

print(cnt)