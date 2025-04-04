import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def find_route(x, w):
    global result, idx

    if len(arr[x]) == 1 and idx != x:
        result = max(result, w)
        return
    
    for ele in arr[x]:
        if ele[0] == 1:
            weight[x].append(w + ele[1])
            continue
        
        if not visited[ele[0]]:
            visited[ele[0]] = 1
            find_route(ele[0], w + ele[1])

n = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, w = map(int, input().split())
    arr[x].append((y, w))
    arr[y].append((x, w))

child_idx = []

for i in range(1, len(arr)):
    if len(arr[i]) == 1:
        child_idx.append(i)

result = 0

weight = [[] for _ in range(n + 1)]

for idx in child_idx:
    visited = [0] * (n + 1)
    visited[idx] = 1
    find_route(idx, 0)

tmp = []
for ele in weight:
    if ele:
        tmp.append(max(ele))
tmp.sort()

if len(tmp) >= 2:
    print(max(result, tmp[-1] + tmp[-2]))
else:
    print(result)