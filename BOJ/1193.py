up = 1
down = 1

x = int(input())
right = True
for i in range(x):
    if right and up == 1:
        down = down + 1
    elif right:
        donw = down + 1
        up = up - 1
    elif down == 1:
        up = up + 1
    else down == 1:
        up = up + 1
        down = down -1
    print(up, down)