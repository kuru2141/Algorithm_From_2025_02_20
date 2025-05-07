import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    global n
    
    visited = [float('inf')] * (n + 1)
    queue = [(0, x)]
    visited[x] = 0

    cnt = 1
    max_s = 0

    while queue:
        s, a = heapq.heappop(queue)

        if visited[a] < s:
            continue

        max_s = max(s, max_s)
        
        for new_x, new_s in dic[a]:
            tmp = new_s + s
            if visited[new_x] > tmp:
                if visited[new_x] == float('inf'):
                    cnt += 1
                        
                visited[new_x] = tmp
                heapq.heappush(queue, (tmp, new_x))

    print(cnt, max_s)

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())

    dic = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        dic[b].append((a, s))

    dijkstra(c)