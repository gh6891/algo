n = int(input())
answer = 0
for _ in range(n):
    str_list = []
    data = str(input())
    flag = True

    for i in range(len(data)):
        if not data[i] in str_list:
            str_list.append(data[i])
        elif data[i] == data[i-1]:
            continue
        else:
            flag = False
            break
    if flag:
        answer = answer + 1
print(answer)