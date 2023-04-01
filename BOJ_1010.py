def factorial(num):
    if(num==0):
        return 1
    else:
        return num * factorial(num-1)

T = int(input())

for i in range(T):
    N,M=map(int,input().split())
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))