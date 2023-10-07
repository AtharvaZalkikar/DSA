#Write a program to determine if given number is palindrome or not. 
#Print true if it is palindrome, false otherwise.

#Write Code here
def checkPalindrome(num):
    a = num
    rev = 0
    while (a != 0):                 # First find the reverse of a number
        n = a % 10                   
        rev = rev*10 + n
        a = a//10
    if (num == rev):                # then check whether the reverse of number is equal to the given input
        return True                 # if yes return 'True' hence numbe is pallindrome else it is not
    else:
        return False

        
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')