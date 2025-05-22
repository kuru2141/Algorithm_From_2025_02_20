import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

cnt = 0

i = 0
while i < N:
    left = 0
    right = N - 1

    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue
        
        tmp = arr[left] + arr[right]

        if tmp == arr[i]:
            cnt += 1
            break

        if tmp > arr[i]:
            right -= 1
        else:
            left += 1

    i += 1

print(cnt)