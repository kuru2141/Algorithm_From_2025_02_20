import heapq
import sys
input = sys.stdin.readline

N = int(input())

queue = []

for _ in range(N):
    tmp = int(input())
    
    if not tmp:
        if not queue:
            print(0)
            continue
        print(heapq.heappop(queue))
    else:
        heapq.heappush(queue, tmp)