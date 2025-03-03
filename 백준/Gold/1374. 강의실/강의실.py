import heapq
import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
    
else:
    arr = []
    for _ in range(N):
        _, a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()

    queue = []
    queue.append(heapq.heappop(arr)[1])
    len_queue = 1

    while arr:
        a, b = heapq.heappop(arr)

        x = heapq.heappop(queue)

        if x > a:
            heapq.heappush(queue, x)
        heapq.heappush(queue, b)
        
        len_queue = max(len_queue, len(queue))

    print(len_queue)