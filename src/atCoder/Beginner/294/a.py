n = input()

a = list(map(int, input().split()))

ans = list(filter(lambda x: x % 2 == 0, a))

print(ans)
