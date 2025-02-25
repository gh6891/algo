import sys

N = int(sys.stdin.readline())
for _ in range(N):
    answer = ""
    sentence = list(sys.stdin.readline().split())
    for j in range(len(sentence)):
        answer = answer + sentence[j][::-1] + " "
    print(answer)
