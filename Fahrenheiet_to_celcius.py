# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, 
# into their corresponding Celsius values and print the table.


def printTable(start,end,step):
    while start<=end:
        c = ((start-32)*5/9)               # dont write '5//9' bcoz it gives zero    
        print(start,int(c))                # Expected output is in integer format so out 'int(C)' 
        start = start + step

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)

