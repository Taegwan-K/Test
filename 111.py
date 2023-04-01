def R(lis:list):
    lis.reverse()
    return

def D(lis:list):
    lis.pop(0)
    return

T = int(input())

for i in range(T):
    command = input()
    n = int(input())
    lis = list(map(int,input().split(',')))
    for x in command:
        if x == 'R':
            R(lis)
        elif x == 'D':
            D(lis)
    print(lis)
