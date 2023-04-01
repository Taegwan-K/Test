N = int(input())

for i in range(1,2*N,2):
    print(" "*int(N-((i+1)/2)),end="")
    print("*"*i)