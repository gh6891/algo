N = int(input())
answer = 0
for i in range(1, N):
    number = int(i)
    answer = number
    while number != 0 :
        answer = answer + number % 10
        number = number // 10
    if answer == N:
        answer = i
        break
    answer = 0
print(answer)