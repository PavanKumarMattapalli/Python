def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
a=int(input("enter a number:"))
if prime(a):
    print(a,"is prime")

while True:
    a+=1
    if prime(a):
        print(a,'is prime')
        break
