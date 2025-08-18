def solution(genres, plays):
    dic = dict()
    lst = list()

    for i in range(len(genres)):
        tmp = genres[i]
        if tmp not in dic:
            dic[tmp] = [plays[i], [(plays[i], i)]]
        else:
            dic[tmp][0] += plays[i]
            dic[tmp][1].append((plays[i], i))

    for ele in dic:
        dic[ele][1].sort(key = lambda x: (x[0], -x[1]), reverse = True)
        lst.append((dic[ele][0], ele))

    lst.sort(key = lambda x: x[0], reverse = True)

    answer = []

    for ele in lst:
        i = 0
        for e in dic[ele[1]][1]:
            if i < 2:
                answer.append(e[1])
                i += 1
            else:
                break
            
    return answer