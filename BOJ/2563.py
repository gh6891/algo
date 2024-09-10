paper = [[0]* 100]*100

answer = 0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if x + i < 100 and y + j < 100:
                paper[x+ i - 1][y + j - 1] = 1
print(paper)
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            answer = answer + 1

print(answer)