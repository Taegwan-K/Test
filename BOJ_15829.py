L = int(input())
arr = input()
tot = 0
pow = 1
for i in arr:
    tot += ((ord(i)-96)*pow)
    pow = pow * 31

print(tot%1234567891)