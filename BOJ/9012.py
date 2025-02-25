import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    stack = []
    flag = 0
    command = sys.stdin.readline().rstrip()
    for i in range(len(command)):
        if command[i] == "(":
            stack.append("(")
        elif len(stack) != 0:
            stack.pop()
        else:
            flag = 1
            break
    if flag == 0 and len(stack) == 0:
        print("YES")
    else:
        print("NO")