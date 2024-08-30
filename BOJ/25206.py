grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_credit = 0.0
total_score = 0.0

for i in range(20):
    a = list(map(str, input().split()))
    credit = float(a[1])
    if a[2] == "P":
        continue
    else:
        total_credit = total_credit + float(a[1])
        total_score = total_score + score_list[grade_list.index(a[2])] * float(a[1])
print(total_score/total_credit)