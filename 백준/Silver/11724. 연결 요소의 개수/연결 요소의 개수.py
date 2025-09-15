import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0 for _ in range(N + 1)]

dic = dict()

for _ in range(M):
    u, v = map(int, input().split())

    if u in dic:
        dic[u].append(v)
    else:
        dic[u] = [v]

    if v in dic:
        dic[v].append(u)
    else:
        dic[v] = [u]

x = 1
visited[1] = x

for i in range(1, N + 1):
    if i in dic:
        for e in dic[i]:
            if visited[i]:
                visited[e] = visited[i]
            else:
                visited[e] = x
    else:
        visited[i] = x
    x += 1

print(len(set(visited[1:])))