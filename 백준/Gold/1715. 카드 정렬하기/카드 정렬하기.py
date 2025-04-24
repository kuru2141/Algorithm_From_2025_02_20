import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    heapq.heappush(arr, int(input()))

result = 0

while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    heapq.heappush(arr, a + b)
    result += a + b

print(result)