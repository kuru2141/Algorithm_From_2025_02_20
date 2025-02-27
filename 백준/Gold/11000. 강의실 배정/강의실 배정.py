import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()

max_class = 0
class_queue = []

for ele in arr:
    if not class_queue:
        heapq.heappush(class_queue, ele[1])
        continue

    tmp = heapq.heappop(class_queue)
    heapq.heappush(class_queue, ele[1])
    
    if tmp > ele[0]:
        heapq.heappush(class_queue, tmp)

    max_class = max(max_class, len(class_queue))

print(max_class)