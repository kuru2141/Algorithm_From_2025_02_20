K = int(input())

arr = []

for _ in range(K):
    input_num = int(input())
    if input_num == 0:
        if not arr:
            continue
        arr.pop()
    else:
        arr.append(input_num)

print(sum(arr))