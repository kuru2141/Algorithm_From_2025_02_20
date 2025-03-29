import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr_1 = [input().strip() for _ in range(N)]
arr_2 = [input().strip() for _ in range(M)]

dic = dict()

for ele in (arr_1 + arr_2):
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] += 1

tmp = list(dic.keys())
tmp.sort()


result = []
for key in tmp:
    if dic[key] > 1:
        result.append(key)

print(len(result))
for ele in result:
    print(ele)