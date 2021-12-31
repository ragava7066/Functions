#function to control the program -> main
#function to get all numbers in given series
#function to find prime numbers in given series
#function to count all the factors
#display the result


def main():
    num1 = int(input('enter starting number : '))
    num2 = int(input('enter ending number : '))
    _prime = is_prime(num1&num2)
    print_prime_or_not(_prime , num1&num2)
    

def is_prime(num):
    if count_of_factors(num) == 2:
        return True
    return False


def count_of_factors(num):     
    count=int()
    for div in range(1 , num+ 1):
        if num%div == 0:
            count = sum(count,1)
        return count


def print_prime_or_not(flag,num):
    if flag is True:
        print(f'{num} is prime')
    else:
         print(f'{num} is not prime')   

main()
