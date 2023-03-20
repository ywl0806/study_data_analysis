from collections import *

N, M = map(int, input().split())


parent = defaultdict(int)

for i in range(1, N + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x
    return


count = 0
for _ in range(M):
    a, _, c, _ = input().split()
    a = find(int(a))
    c = find(int(c))
    if parent[a] != parent[c]:
        union(a, c)
    else:
        count += 1

print(count, N - M)
