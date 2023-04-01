count = int(input())

num_list = input().split(' ')

max = int(num_list[0])

for i in range(0,count):
    if max<int(num_list[i]):
        max = int(num_list[i])

min = int(num_list[0])

for j in range(0,count):
    if min>int(num_list[j]):
        min = int(num_list[j])

print(min,max)