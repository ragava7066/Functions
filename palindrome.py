# function to control everything -> main

def main():
    num = int(input('enter a number : '))
    _palindrome = is_palindrome(num)
    print_palindrome_or_not(_palindrome , num)
    
#function to check if it is palindrome or not    
def is_palindrome(num):
    if num==reverse(num):
        return True
    return False

#function to reverse all factors
def reverse(num):  
    temp=num   
    res=0 
    while (temp):
        last_digit = temp%10
        res= res*10 +last_digit
        temp=temp//10
    return res

#display the result
def print_palindrome_or_not(flag,num):
    if flag is True:
        print(f'{num} is palindrome')
    else:
         print(f'{num} is not palindrome')   

main()