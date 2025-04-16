import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    X = int(''.join(map(str, input().split())))
    Y = int(''.join(map(str, input().split())))
    state = list(map(int, input().split()))

    new_state = state * 2

    cnt = 0
    for i in range(len(state)):
        tmp = int(''.join(map(str, new_state[i : i + M])))
        if tmp >= X and tmp <= Y:
            cnt += 1
    print(cnt)