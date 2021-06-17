a=input()
def fun(a):
    if a is '':
        return 0
    else:
        return(1+fun(a[1: ]))
print(fun(a))
