def factorial(num):
    if(num<=1):
        return 1
    else:
        return num * factorial(num - 1)
    
N = int(input())
N = list(str(int(factorial(N))))
cnt = 0
numlen = len(N)
for i in range(-1,-(numlen+1),-1):
    if N[i] == '0':
        cnt+=1
    elif N[i] != '0':
        print(cnt)
        break