
def main():
    print('This code prints all the palindrome numbers in given range')
    lower_limit = read('Enter lower_limit : ')
    upper_limit = read('Enter upper_limit : ')
    print_palindrome_numbers(lower_limit , upper_limit)

def read(msg):
    return int(input(msg))

def print_palindrome_numbers(lower_limit , upper_limit):
    for num in range(lower_limit , upper_limit):
        if is_palindrome(num) is True:
            print(f'{num} is palindrome')

def is_palindrome(num):
    if num == reverse(num):
        return True
    return False

def reverse(num):
    temp=num
    res=0
    while(temp):
        last_digit = temp %10
        temp = temp// 10
        res = res*10+last_digit
    return res

main()
