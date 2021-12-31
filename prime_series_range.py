def main():
    print('this code prints all prime numbers in given range')
    lower_limit = read('Enter lower_limit : ')
    upper_limit = read('Enter upper_limit : ')
    print_prime_numbers(lower_limit,upper_limit)

def read(msg):
    return int(input(msg))

def print_prime_numbers(lower_limit , upper_limit):
    for num in range(lower_limit , upper_limit):
        if is_prime (num) is True:
            print(f'{num} is prime')

def is_prime(num):
    if count_of_factors(num) == 2:
        return True
    return False
def count_of_factors(num):     
    count=int()
    for div in range(1 , num+ 1):
        if num%div == 0:
            count = sum((count,1))
    return count
main()