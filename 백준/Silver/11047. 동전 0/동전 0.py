import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [(i, int(input())) for i in range(N, 0, -1)]
arr.sort(key = lambda x: x[0])
queue = [K]

result = 0

while True:
    _, money = heapq.heappop(arr)

    k = queue.pop()

    if k >= money:
        result += k // money
        if K % money == 0:
            break
        queue.append(k % money)
    else:
        queue.append(k)

print(result)