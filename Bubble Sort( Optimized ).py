def bubble_Sort(A):
    for i in range(len(A)-1):  # bcoz we dont need the final pass
        for j in range(len(A)-1-i):  #for every iteration or pass we dont have to sort every element as no of passes increases more elemnts get sorted
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A

#bubble_Sort([9,5,7,3,1,4])

Arr = [int(x) for x in input("Enter array: ").split()]
bubble_Sort(Arr)
for k in Arr:                            #to get output in space seperated form
    print(k, end= " ")
