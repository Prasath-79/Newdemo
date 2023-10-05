print( '1.addition(+)\n 2.subtraction(-)\n 3.multiplication(*)\n 4.division(/)')
x=int(input('enter the first value:'))
y=int(input('enter the second value:'))
operation=int(input('enter the operation:'))
if operation==1:
    print(x+y)
elif operation==2:
    print(x-y)
elif operation==3:
    print(x*y)
elif operation==4:
    print(x/y)
else:
    print('enter the correct operation')

# Factorial
num=int(input('Enter the number:'))
factorial=1
if num<=0:
    print('Negative number does not have factorial')
elif num==0:
    print('Factorial of 0 is 1')
else:
    for i in range(1,num+1):
        factorial*=i
    print(factorial)