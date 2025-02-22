tmp = int(input())

for _ in range(tmp):
    n = int(input())

    arr = [list(map(str, input().split())) for _ in range(n)]

    dic = dict()

    for i in range(n):
        x = arr[i][1]
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    result = 1
    for ele in dic.values():
        result *= (ele + 1)
        # 각 옷별로 0개 또는 1개씩 입을 수 있음

    print(result - 1) # 모두 입지 않은 경우 제거