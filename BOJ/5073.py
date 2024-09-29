while True:
    length = list(map(int, input().split()))
    if length[0] == length[1] == length[2] == 0:
        break
    length.sort()
    if length[2] >= length[0] + length[1]:
        print("Invalid")
    elif length[0] == length[1] == length[2]:
        print("Equilateral ")
    elif length[0] == length[1] or length[1] == length[2] or length[0] == length[2]:
        print("Isosceles ")
    else:
        print("Scalene ")
