N = int(input())

arr = [input().split() for _ in range(N)]

result_arr = []

for sen in arr:
    ch = 0
    
    for i in range(len(sen)):
        if sen[i][0].lower() not in result_arr and sen[i][0].upper() not in result_arr:
            result_arr.append(sen[i][0])
            sen[i] = '[' + sen[i][0] + ']' + sen[i][1:]
            ch = 1
            break
        
    if ch:
        continue
        
    for i in range(len(sen)):
        if ch:
            break
        
        for j in range(len(sen[i])):
            if sen[i][j].lower() not in result_arr and sen[i][j].upper() not in result_arr:
                result_arr.append(sen[i][j])
                sen[i] = sen[i][:j] + '[' + sen[i][j] + ']' + sen[i][j + 1:]
                ch = 1
                break

for sen in arr:
    print(' '.join(sen))