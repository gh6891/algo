n = int(input())

for i in range(1, n):
    a = " " * (n - i) + "*" * (2 * i - 1)
    print(a)

for i in range(n):
    a = " " * i + "*" * (2 * n - 1 - 2 * i)
    print(a)