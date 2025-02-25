import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        stack.append(command[1])
        continue
    elif command[0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
            continue
        else:
            print(-1)
            continue
    elif command[0] == "size":
        print(len(stack))
        continue
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
            continue
        else:
            print(0)
            continue
    elif command[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
            continue
        else:
            print(-1)
            continue