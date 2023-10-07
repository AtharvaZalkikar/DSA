# An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself. For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

# Example: Input: 'n' = 1634

# Output: true

# Explanation: 1634 is an Armstrong number, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

#--------------------------------------------------------------------------------------------------------------------------


## Read input as specified in the question.
## Print output as specified in the question
num = int(input())

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print('true')
else:
   print('false')

