for _ in range(3):
    N = int(input())
    S = 0

    for _ in range(N):
        S += int(input())

    if S == 0:
        print(0)
    elif S > 0:
        print('+')
    else:
        print('-')