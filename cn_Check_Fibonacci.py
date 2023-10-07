
def checkMember(n):
    a = 0 
    b = 1                                        
    c = -1 
    for i in range(n) :
        c = a + b 
        a = b 
        b = c 
        if (c == n):
            return True
            break
        
    

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")

    # though still we dont know how to give output true if n ==0....
