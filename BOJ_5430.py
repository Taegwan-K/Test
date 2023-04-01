def R(lis:list):
    lis.reverse()
    return

def D(lis:list):
    lis.pop(0)
    return

T = int(input())
flag = 0

for i in range(T):
    command = input()
    n = int(input())
    lis = list(map(int,input()))
    #lis.remove('[')
    #lis.remove(']')
    #while(len(lis) != n):
    #    lis.remove(',')
    #lis = list(map(int,lis))
    for x in command:
        if x == 'R':
            R(lis)
        elif x == 'D':
            try: D(lis)
            except:
                print("error")
                flag = 1
    if(flag!=1):
        print(lis)