import sys
input = sys.stdin.readline

def checkDp(left, right):
    if left < right and dp[left][right] == 0:
        return 0
    return 1

N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

length = 0
while length < N:
    for i in range(N - length):
        if arr[i] == arr[i + length]:
            left = i + 1
            right = i + length - 1

            if not (left < right and dp[left][right] == 0):
                dp[i][i + length] = 1
                
    length += 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    
    S -= 1
    E -= 1

    print(dp[S][E])
