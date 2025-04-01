def solution(a, b, c, d):
    answer = 0
    
    arr = [a, b, c, d]
    dic = dict()
    
    for ele in arr:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] += 1

    if len(dic) == 1:
        answer = 1111 * list(dic.keys())[0]
        
    elif len(dic) == 2:
        for x in dic.keys():
            if dic[x] == 3:
                a = x
                tmp = list(dic.keys())
                tmp.remove(a)
                b = tmp[0]
                answer = (10 * a + b) ** 2
                break

            if dic[x] == 2:
                a = x
                tmp = list(dic.keys())
                tmp.remove(a)
                b = tmp[0]
                answer = (a + b) * abs(a - b)
                break

    elif len(dic) == 3:
        for x in dic.keys():
            if dic[x] == 2:
                a = x
                tmp = list(dic.keys())
                tmp.remove(a)
                b = tmp[0]
                c = tmp[1]
                answer = b * c
                break

    else:
        answer = min(arr)

    return answer