import sys

N = int(sys.stdin.readline())
answer = ""
stack = [] #숫자들 정리하는 곳
data_stack = [] #만들어야할 수열 넣는 곳
for _ in range(N):
    data = int(sys.stdin.readline())
    data_stack.append(data)

for i in range(1, N+1):
    stack.append(i)
    
    answer = answer + "+" + "\n"

    if len(data_stack) == 0:
        break
    print("data", data_stack)
    print("stack", stack)
    while stack[-1] == data_stack[0]: #스택과 데이터끝스택이 다르면 끝
        
        print("data", data_stack)
        print("stack", stack)

        stack.pop()
        data_stack.pop(0)
        answer = answer + "-" + "\n"
        if len(data_stack) == 0:
            break
        
print(answer)