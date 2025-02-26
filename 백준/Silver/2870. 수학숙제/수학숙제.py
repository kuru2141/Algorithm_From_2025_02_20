N = int(input())

arr = []

for _ in range(N):
    arr.append(input())

num_list = []

for ele in arr:
    tmp = ''
    for i in range(len(ele)):
        if ele[i].isnumeric():
            tmp += ele[i]
            if i == len(ele) - 1:
                num_list.append(int(tmp))
                tmp = ''
        else:
            if tmp != '':
                num_list.append(int(tmp))
                tmp = ''
                
num_list.sort()

for ele in num_list:
    print(ele)