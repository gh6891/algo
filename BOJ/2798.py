answer = 0
N, M = input().split()
N = int(N)
M = int(M)

nlist = list(map(int, input().split()))
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            value = nlist[i] + nlist[j] + nlist[k]
            if value <= M and value > answer:
                answer = value
print(answer)
