alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

input_data = input()

for alpha in alpha_list:
    input_data = input_data.replace(alpha, "*")
print(len(input_data))