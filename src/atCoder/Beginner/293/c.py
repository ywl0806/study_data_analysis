h, w = list(map(int, input().split()))

yo = []
for i in range(h):
    yo.append(list(input().split()))
count = []


def func(x, y, stk):
    if yo[x][y] in stk:
        return 1

    if x >= h-1 and y >= w-1:
        count.append(1)
        return 0

    stk.append(yo[x][y])

    po = []
    if x < h - 1:
        po.append([x + 1, y])
    if y < w - 1:
        po.append([x, y + 1])

    for pi in po:
        print(pi)
        func(pi[0], pi[1], stk)
    stk.pop()


sta = []
func(0, 0, sta)

print(len(count))
