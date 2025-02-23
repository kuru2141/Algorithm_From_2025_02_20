X, Y = input().split()

X = [e for e in X]
Y = [e for e in Y]

X.reverse()
Y.reverse()

tmp = str(int(''.join(X)) + int(''.join(Y)))

tmp_list = [e for e in tmp]
tmp_list.reverse()

print(int(''.join(tmp_list)))