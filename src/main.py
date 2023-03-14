import csv
import os

path = os.getcwd()
print(path)

count = 0
f = open("csv/test.csv", "r")
reader = csv.reader(f)

hoge = reader[0]

print(hoge)
for line in reader:
    print(line)
    count += 1
    if count > 10:
        break

f.close()
