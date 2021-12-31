# function to control everything -> main
def main():
    num = int(input('enter a number : '))
    _prime = is_prime(num)
    print_prime_or_not(_prime , num)
    
#function to check if it is prime or not    
def is_prime(num):
    if count_of_factors == 2:
        return True
    return False

#function to count all factors
def count_of_factors(num):     
    count=int()
    for div in range(1 , num+ 1):
        if num%div == 0:
            count = sum(count,1)
    return count


#display the result
def print_prime_or_not(flag,num):
    if flag is True:
        print(f'{num} is prime')
    else:
         print(f'{num} is not prime')   

main()