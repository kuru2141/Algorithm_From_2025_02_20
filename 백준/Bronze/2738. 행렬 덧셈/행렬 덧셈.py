N, M = map(int, input().split())

arr_1 = [[int(e) for e in input().split()] for _ in range(N)]
arr_2 = [[int(e) for e in input().split()] for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(arr_1[i][j] + arr_2[i][j], end = ' ')
    print()