def solution(today, terms, privacies):
    year, month, day = list(map(int, today.split('.')))
    
    new_terms = dict()
    new_privacies = []
    result = []
    idx = 0

    for t in terms:
        x, y = t.split()
        new_terms[x] = int(y)

    for p in privacies:
        idx += 1

        x, y = p.split()
        a, b, c = list(map(int, x.split('.')))

        t = new_terms[y]
        b += t
        while b > 12:
            b -= 12
            a += 1

        c -= 1
        if c == 0:
            b -= 1
            c += 28
            if b == 0:
                a -= 1
                b += 12

        if a < year:
            result.append(idx)
        elif a > year:
            continue
        elif b < month:
            result.append(idx)
        elif b > month:
            continue
        elif c < day:
            result.append(idx)
        elif c > day:
            continue
    
    return result