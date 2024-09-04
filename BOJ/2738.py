n, m = map(int, input().split())

mat_a = []
mat_b = []

for i in range(2 * n):
    if i < n:
        mat_a.append(list(map(int,input().split())))
    else:
        mat_b.append(list(map(int,input().split())))

for i in range(n):
    output = ""
    for j in range(m):
        output = output + str(mat_a[i][j] + mat_b[i][j]) + " "
    print(output)