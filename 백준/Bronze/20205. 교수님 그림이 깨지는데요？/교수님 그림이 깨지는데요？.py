from collections import deque

N, K = map(int, input().split())

arr = []
new_arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    tmp_arr = []
    queue = deque(arr[i])
    
    while queue:
        tmp = queue.popleft()
        for _ in range(K):
            tmp_arr.append(tmp)

    for _ in range(K):
        new_arr.append(tmp_arr)

for i in range(N * K):
    for j in range(N * K):
        print(new_arr[i][j], end = ' ')
    print('')