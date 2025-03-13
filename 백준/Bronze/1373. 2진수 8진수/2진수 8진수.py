word = input()
while len(word) % 3 != 0:
    word = '0' + word

i = 0
arr = []
while i < len(word):
    arr.append(word[i] + word[i + 1] + word[i + 2])
    i += 3

result = ''
for ele in arr:
    tmp = 0
    j = 1
    for i in range(2, -1, -1):
        tmp += j * int(ele[i])
        j *= 2
    result += str(tmp)
    
print(result)
