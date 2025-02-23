word = input()
word = word.upper()
dic = dict()

for ele in word:
    if ele not in dic:
        dic[ele] = 1
    else:
        dic[ele] += 1

list_ele = []

for ele in dic:
    if dic[ele] == max(dic.values()):
        list_ele.append(ele)

if len(list_ele) == 1:
    print(list_ele[0])
else:
    print('?')