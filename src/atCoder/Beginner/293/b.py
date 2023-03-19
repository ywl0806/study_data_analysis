n = int(input())
ele = input()

inputArr = ele.split(" ")

for i in range(len(inputArr)):
    inputArr[i] = int(inputArr[i])

for i, val in enumerate(inputArr):
    if (val != 0):
        inputArr[val - 1] = 0
ans = []

for i, an in enumerate(inputArr):
    if (an != 0):
        ans.append(i + 1)

print(len(ans))
anstr = ""
for v in ans:
    anstr += str(v) + " "
print(anstr)
