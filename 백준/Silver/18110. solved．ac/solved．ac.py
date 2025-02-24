import sys
input = sys.stdin.readline
# 입력이 많아서 일반적인 input() 쓰면 시간초과

def round_int(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(input())

if n == 0:
    print(0)
else:
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    tmp = round_int(n * 0.15)
    # 파이썬의 round는 오사오입 사용
    arr = arr[tmp: n - tmp]

    print(round_int(sum(arr) / len(arr)))