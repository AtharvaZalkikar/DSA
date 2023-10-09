def bubble_Sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

Arr = [int(x) for x in input("Enter array: ").split()]
bubble_Sort(Arr)
for k in Arr:                            #to get output in space seperated form
    print(k, end= " ")
