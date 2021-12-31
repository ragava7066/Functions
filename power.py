def power(num, power):
    return(num ** power)
num = int(input('enter a number :'))
powr = int(input('enter a power :'))
res = power(num,powr)
def even_or_odd(num):
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')    
even_or_odd(res)    
   