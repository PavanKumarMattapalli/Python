n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()




for i in range(65,65+n):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()
