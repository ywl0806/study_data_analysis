n, m = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A + B)

ans = {c: i + 1 for i, c in enumerate(C)}

for a in A:
    print(ans[a])

for b in B:
    print(ans[b])