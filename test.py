import sys

sentence = list(sys.stdin.readline().split())

for i in range(len(sentence)):
    print(reversed(sentence[i]))