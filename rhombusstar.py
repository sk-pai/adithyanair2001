n=int(input())

for i in range(0,n):
    for l in range(0,i):
        print(" ",end="")
    
    for j in range(0,n):
        print("*",end="")

    print()