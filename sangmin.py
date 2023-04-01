T = int(input())
clothes = {}
for a in range(T):
    clothes.clear()
    cnt = 1
    n = int(input())

    for b in range(n):
        A,B = map(str,input().split())
        if B in clothes:
            clothes[B] = clothes[B]+1
        else:
            clothes[B] = 1
    clothes_list = list(clothes.values())
    for b in clothes_list:
        cnt *= b+1
    print(cnt-1)
