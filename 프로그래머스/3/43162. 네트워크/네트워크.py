def find(a, parent):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a], parent)
    return parent[a]
    
def union(a, b, parent):
    aRoot = find(a, parent)
    bRoot = find(b, parent)

    if aRoot != bRoot:
        if aRoot <= bRoot:
            parent[bRoot] = aRoot
        else:
            parent[aRoot] = bRoot

def solution(n, computers):
    parent = [e for e in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if computers[i - 1][j - 1]:
                union(i, j, parent)

    for i in range(1, n + 1):
        parent[i] = find(i, parent)
                
    return len(set(parent[1:]))