from sortedcontainers import SortedSet

n, q = map(int, input().split())

called = SortedSet()

ncMin = 1

ans = set()
for i in range(q):
    e = list(input())

    if e[0] == "1":
        called.add(ncMin)
        ncMin += 1

    if e[0] == "2":
        called.remove(int(e[2]))

    if e[0] == "3":
        ans.add(min(called))

for an in ans:
    print(an)
