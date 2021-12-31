def main():
    n=input('enter a number : ')
    print('this code checks if given number is armstrong or not')
    print_armstrong_or_not(int(n)) if n.isnumeric() else print_armstrong_or_not()

def armstrong(num):
    power= count_of_digits(num)
    res=int()
    while num:
        last_digit =num%10
        res=sum((res,pow(last_digit,power)))
        num=remove_last_digit(num)
    return res

def count_of_digits(num):
    count=int()
    while num:
        num=remove_last_digit(num)
        count=sum((count,1))
    return count


def remove_last_digit(num):
    return num//10

def print_armstrong_or_not(n=12):
    num=1
    count=0
    while count<n :
        if armstrong(num) == num:
            print(f'{num} is an armstrong')
            count=sum((count,1))
        num=sum((num,1))

main()



