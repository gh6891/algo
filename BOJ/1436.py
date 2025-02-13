N = int(input())
count = 0
i = 666
while count != N:
    check = str(i)
    if "666" in check:
        count = count+1
    i = i + 1
print(i - 1)