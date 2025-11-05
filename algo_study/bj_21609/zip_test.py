arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_arr = list(map(list, zip(*arr[:])))[::-1]

for i in range(3):
    print(new_arr[i])