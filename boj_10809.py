S = list(input())
for i in range(ord('a'),ord('z')+1):
    for j in range(0,len(S)):
        if chr(i) == S[j]:
            print(j,end=" ")
            break
        if j==len(S)-1:
            print("-1",end=" ")