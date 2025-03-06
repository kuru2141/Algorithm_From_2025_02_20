from itertools import combinations

L, C = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()

m_arr = ['a', 'e', 'i', 'o', 'u']

for ele in combinations(arr, L):
    m_len = 0
    j_len = 0
    
    for e in ele:
        if e in m_arr:
            m_len += 1
        else:
            j_len += 1

    if m_len > 0 and j_len > 1:
        print(''.join(ele))