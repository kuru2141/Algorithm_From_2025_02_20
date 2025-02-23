A, B, C, D = map(int, input().split())

arr = list(map(int, input().split()))

for ele in arr:
    cnt = 0

    if ele % (A + B) <= A and ele % (A + B) > 0:
        cnt += 1

    if ele % (C + D) <= C and ele % (C + D) > 0:
        cnt += 1

    print(cnt)