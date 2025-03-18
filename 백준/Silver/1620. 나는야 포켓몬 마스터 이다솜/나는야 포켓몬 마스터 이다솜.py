import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic_1 = dict()
dic_2 = dict()
for i in range(1, N + 1):
    tmp = input().strip()
    dic_1[i] = tmp
    dic_2[tmp] = i

for _ in range(M):
    word = input().strip()
    if word[0].isnumeric():
        print(dic_1[int(word)])
    else:
        print(dic_2[word])