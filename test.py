lis = "abcdefghijklmnopqrstuvwxyz"
cnt = 0
for i in lis:
    print(i+':',end=' ')
    print(('0'*cnt),end='')
    cnt+=1
    if i!='z':
        print('1')
