import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    arr = [[i for i in range(1, n + 1)]]

    for i in range(1, k + 1):
        arr.append([])
        for j in range(1, n + 1):
            tmp = sum(arr[i - 1][:j])
            arr[-1].append(tmp)
 
    print(sum(arr[k - 1][:n]))