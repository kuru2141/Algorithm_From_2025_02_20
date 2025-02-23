N = int(input())

tmp_list = []

tmp_list.append(0)
tmp_list.append(1)

for i in range(2, N + 1):
    tmp_list.append(tmp_list[i - 2] + tmp_list[i - 1])

print(tmp_list[N])