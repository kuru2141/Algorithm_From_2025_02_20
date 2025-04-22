def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        tmp = ''
        dic = dict()
        new_s = s
        
        while new_s:
            word = new_s[:i]
            k = 0
            t = 0
            while t < len(s) + 1:
                if word == new_s[t:t + i]:
                    k += 1
                    t += i
                else:
                    if k == 1:
                        tmp += word
                    else:
                        tmp += str(k) + word
                    break
            new_s = new_s[t:]
        result.append(len(tmp))
    return min(result)