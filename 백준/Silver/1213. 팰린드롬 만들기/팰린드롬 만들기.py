import sys
input = sys.stdin.readline

sen = input().strip()
dic = dict()

for i in range(len(sen)):
    if sen[i] in dic:
        dic[sen[i]] += 1
    else:
        dic[sen[i]] = 1

cnt = 0

for ele in dic.keys():
    if dic[ele] % 2 == 1:
        cnt += 1

    if cnt > 1:
        break

if cnt == 2:
    print('I\'m Sorry Hansoo')
else:
    tmp = ''
    result = ''

    for ele in sorted(dic.keys()):
        if dic[ele] % 2 == 0:
            result += ele * (dic[ele] // 2)
        else:
            result += ele * ((dic[ele] - 1) // 2)
            tmp = ele

    result = result + tmp + ''.join(sorted(result, reverse = True))
    print(result)