# function to control everything -> main
def main():
    num = int(input('enter a number : '))
    _perfect = is_perfect(num)
    print_perfect_or_not(_perfect , num)
    
#function to check if it is perfect or not  
def is_perfect(num):
    if num == sum_of_factors(num):
        return True
    return False

#function to sum all factors
def sum_of_factors(num):     
    res = 0
    for div in range(1 , num//2 + 1):
        if num%div == 0:
            res = add(res , div)
    return res

#function to add 2 ints
def add(num1,num2):
    return num1 + num2

#display the result
def print_perfect_or_not(flag,num):
    if flag is True:
        print(f'{num} is perfect')
    else:
         print(f'{num} is not perfect')   

main()