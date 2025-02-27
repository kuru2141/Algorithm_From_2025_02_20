H, W = map(int, input().split())

def check_cloud(arr, result_arr, x):
    global H, W

    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'c' and result_arr[i][j] == -1:
                result_arr[i][j] = x
    return

arr = []
result_arr = []

for _ in range(H):
    arr.append(list(e for e in input()))
    result_arr.append(list(-1 for _ in range(W)))

check_cloud(arr, result_arr, 0)

for x in range(1, W):
    for i in range(H):
        arr[i] = ['.'] + arr[i][:-1]
    check_cloud(arr, result_arr, x)

for i in range(H):
    for j in range(W):
        print(result_arr[i][j], end = ' ')
    print('')