H, W = map(int, input().split())

ans = []

for h in range(H):
    X = map(int, input().split())
    ans.append(["." if x == 0 else chr(64 + x) for x in X])

for an in ans:
    print(" ".join(an))
