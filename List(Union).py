a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
   if i not in a:
       a.append(i)
print(a)
