n = int(input())
line = 1
a, b = 0, 0
while True:
    if n <= line * (line + 1) / 2:
        break
    line = line + 1
if line % 2 == 0:
    a = n - line*(line-1)/2
    b = line*(line + 1)/2 -n +1
else:

    b = n-line*(line-1)/2
    a = line*(line + 1)/2 - n + 1
a = str(int(a))
b = str(int(b))
print(a+"/"+ b)