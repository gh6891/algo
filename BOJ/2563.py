paper = [[0]*100 for _ in range(100)]
answer = 0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if x + i  < 100 and y + j < 100:
                paper[x+ i][y + j] = 1

for x in range(100):
    for y in range(100):
        if paper[x][y] == 1:
            answer = answer + 1

print(answer)