M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    #소수 검사
    for j in range(2, i+1):
        if i == 1:
            break
        if i % j == 0:
            if j == i:
                prime.append(i)
            break
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])