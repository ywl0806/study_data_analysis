s = "ababababa"
listStr = list(s)
for i in range(1, len(s), 2):
    listStr[i], listStr[i-1] = listStr[i-1], listStr[i]
    i += 2
print("".join(listStr))
