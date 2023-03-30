a, x, m = map(int, input().split())

result = x % m if a == 1 else ((1 - pow(a, x, m)) * pow(1 - a, m - 2, m)) % m

print(result)
