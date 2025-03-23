from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
dic = dict()

for _ in range(M):
    u, v = map(int, input().split())

    if u not in dic:
        dic[u] = [v]
    else:
        dic[u].append(v)

    if v not in dic:
        dic[v] = [u]
    else:
        dic[v].append(u)

for k in dic.keys():
    dic[k].sort(reverse = True)

idx = 1

visited = [0] * (N + 1)
visited[R] = idx

queue = deque()
queue.append(R)

while queue:
    x = queue.popleft()

    if x not in dic:
        continue

    for ele in dic[x]:
        if not visited[ele]:
            idx += 1
            visited[ele] = idx
            queue.append(ele)
            
for i in range(1, len(visited)):
    print(visited[i])