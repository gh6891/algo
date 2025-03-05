import sys

N = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(N)]

operation = []
stack = [] #숫자들 정리하는 곳

current = 1

for num in sequence:
    while current <= num:
        stack.append(current)
        operation.append('+')
        current = current + 1
    
    if stack[-1] == num:
        stack.pop()
        operation.append('-')
    else:
        print("NO")
        exit()
print("\n".join(operation))
