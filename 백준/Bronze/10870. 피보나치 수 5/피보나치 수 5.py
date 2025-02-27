N = int(input())

arr = [0, 1]

if N < 2:
    print(arr[N])
else:
    for i in range(2, N + 1):
        arr.append(arr[i - 2] + arr[i - 1])

    print(arr[-1])