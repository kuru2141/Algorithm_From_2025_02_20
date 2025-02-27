from collections import deque

def check_word(queue, word_list):
    while queue:
        a = queue.popleft()
        if queue:
            b = queue.popleft()
            tmp = a + b
            if tmp in word_list:
                if tmp == 'ch':
                    if queue:
                        c = queue.popleft()
                        if c != 'u':
                            return 'NO'
                    else:
                        return 'NO'
            else:
                return 'NO'
        else:
            return 'NO'
    return 'YES'

S = input()

S_set = set(S)
queue = deque(S)

if S_set <= set(['p', 'i', 'k', 'a', 'c', 'h', 'u']):
    word_list = ['pi', 'ka', 'ch']
    print(check_word(queue, word_list))
else:
    print('NO')