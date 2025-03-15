from collections import deque

N, D = map(int, input().split())
arr = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
arr.sort()

result = deque()
result.append((0, 0))

result_arr = []

while result:
    short_d, total_d = result.popleft()
    if total_d <= D:
        result_arr.append(short_d + (D - total_d))
        
    for i in range(len(arr)):
        x, y, t = arr[i]
        if x >= total_d:
            new_short_d = short_d + x - total_d + t
            new_total_d = y
            result.append((new_short_d, new_total_d))
            
print(min(result_arr))