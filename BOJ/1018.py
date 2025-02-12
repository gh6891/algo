N, M = map(int, input().split())
board = []
answer = 64
for row in range(N):
    board.append(list(input().strip()))

for a in range(0, N-7):
    for b in range(0, M-7):
        count1 = 0
        count2 = 0
        for i in range(8):
            for j in range(8):
                expected1 = "W" if (i+j) % 2 == 0 else "B"
                expected2 = "B" if (i+j) % 2 == 0 else "W"

                if board[i+a][j+b] != expected1:
                    count1 = count1 + 1
                if board[i+a][j+b] != expected2:
                    count2 = count2 + 1
        count = min(count1, count2)
        answer = min(count, answer)
print(answer)