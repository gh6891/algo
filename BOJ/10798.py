voca = []
answer = ""
maxlen = 0
for i in range(5):
    voca.append(list(input()))
    if maxlen < len(voca[i]):
        maxlen = len(voca[i])
for i in range(maxlen):
    for j in range(5):
        if len(voca[j]) == 0:
            continue
        answer = answer + voca[j].pop(0)
print(answer)