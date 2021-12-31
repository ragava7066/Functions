#function to control everything
def main():
    num=int(input('enter a number : '))
    print_armstrong_or_not(_armstrong(num),num)

#function to perform armstrong operations
def _armstrong(num):
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

def print_armstrong_or_not(res,num):
    if res==num:
        print(f'{num} is an armstrong')
    else:
         print(f'{num} is not an armstrong')   

main()

