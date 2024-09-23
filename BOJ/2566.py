maximum = 0
for i in range(9):
    n_array = []
    n_array = list(map(int, input().split()))
    if maximum <= max(n_array):
        maximum = max(n_array)
        n = i + 1
        m = n_array.index(maximum) + 1
print(maximum)
print(n, m) 