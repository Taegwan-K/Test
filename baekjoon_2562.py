num_list = []

for x in range(0,9):
    num_list.append(int(input()))

max = int(num_list[0])

for i in range(0,9):
    if max<int(num_list[i]):
        count = i+1
        max = int(num_list[i])

print(max)
