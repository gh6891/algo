n = int(input())
count = 1
i = 1
while True:
    if n <= i:
        answer = count
        break
    else:
        i = i + 6 * count
        count = count + 1
print(answer)