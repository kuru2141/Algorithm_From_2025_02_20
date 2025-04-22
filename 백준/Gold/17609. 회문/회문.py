import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    tmp = input().strip()

    queue = []
    queue.append((tmp, 0, 0, len(tmp) - 1))

    result = []
    
    while queue:
        word, check, i, j = queue.pop()

        c = 0

        while i < j:
            if word[i] != word[j]:
                if check == 1:
                    c = 1
                    result.append(2)
                    break

                if word[i] == word[j - 1]:
                    queue.append((word, 1, i, j - 1))

                if word[i + 1] == word[j]:
                    queue.append((word, 1, i + 1, j))

                c = 1
                result.append(2)
                break
                
            else:
                i += 1
                j -= 1
            
        if not c:
            if check:
                result.append(1)
            else:
                result.append(0)

    if 0 in result:
        print(0)
    elif 1 in result:
        print(1)
    else:
        print(2)