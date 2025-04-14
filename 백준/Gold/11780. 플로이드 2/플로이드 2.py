import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [[[float('inf'), []] for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    visited[a][b] = visited[a][b] if visited[a][b][0] <= c else [c, [a, b]]
    
for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                continue
            visited[i][j] = visited[i][j] if visited[i][j][0] <= visited[i][k][0] + visited[k][j][0] else [visited[i][k][0] + visited[k][j][0], visited[i][k][1] + visited[k][j][1][1:]]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if visited[i][j][0] == float('inf'):
            print(0, end = ' ')
        else:
            print(visited[i][j][0], end = ' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print(0)
        else:
            print(len(visited[i][j][1]), " ".join(map(str, visited[i][j][1])))