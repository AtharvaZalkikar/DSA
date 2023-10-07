# n = int(input())
# li = [int(x) for x in input().split()]
# ele = int(input())
# isFound = False

# for i in range(len(li)):
#     if li[i] == ele:
#         print(i)
#         isFound = True
#         break
# if isFound is False:
#         print(-1)



# Function Linear Search

def linear_search(li,ele):
    #li is the lis ele is th element to be searched
    
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return -1

li = [1,2,3,4,5,6]
print(linear_search(li,4))
