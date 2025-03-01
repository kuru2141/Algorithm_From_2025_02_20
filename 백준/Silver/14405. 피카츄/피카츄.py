S = input()

S = S.replace('pi', ' ')
S = S.replace('ka', ' ')
S = S.replace('chu', ' ')

if S == ' ' * len(S):
    print('YES')
else:
    print('NO')