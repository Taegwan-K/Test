lis = []
lis_total = 0

total = int(input())
count = int(input())

for x in range(0,count):
    lis += input().split(' ')

for i in range(0,count*2,2):
    lis_total += int(lis[i])*int(lis[i+1])

if lis_total==total:
    print("Yes")
else:
    print("No")