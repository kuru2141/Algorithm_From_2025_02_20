import sys
input = sys.stdin.readline

sentence = input().strip()
num = []
cal = []

i = 0
tmp = ''
while i < len(sentence):
    x = sentence[i]
    if x.isalnum():
        tmp += x
    else:
        num.append(int(tmp))
        cal.append(x)
        tmp = ''
    i += 1
num.append(int(tmp))

result = num[0]
num = num[1:]
tmp = 0

check = 0
for i in range(len(num)):
    if cal[i] == '+':
        if check == 0:
            result += num[i]
        else:
            tmp += num[i]
            if i == len(num) - 1:
                result -= tmp
            
    else:
        tmp += num[i]

        if i == len(num) - 1:
            result -= tmp
        elif cal[i + 1] == '+':
            check = 1
        else:
            result -= tmp
            tmp = 0
            check = 0

print(result)