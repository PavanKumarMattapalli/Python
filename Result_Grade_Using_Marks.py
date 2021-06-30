n=int(input('Enter Subject Marks:'))
if n>90 and n<=100:
    print('O Grade')
elif n>80 and n<=90:
    print('A Grade')
elif n<=80 and n>70:
    print('B Grade')
elif n<=70 and n>60:
    print('C Grade')
elif n<=60 and n>50:
    print('D Grade')
elif n<=50 and n>=35:
    print('E Grade')
else:
    print('Fail')
