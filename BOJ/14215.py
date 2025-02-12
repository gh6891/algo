pole = list(map(int, input().split()))

pole.sort()
if pole[2] >= pole[0]+pole[1]:
    pole[2] = pole[0]+pole[1] -1
print(sum(pole))