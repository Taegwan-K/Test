num = list(input())
cnt = 0
result = ""

num.sort()
num.reverse()

for i in num:
        result += i

if int(result)%30 == 0:
    print(result)
else:
    print("-1")