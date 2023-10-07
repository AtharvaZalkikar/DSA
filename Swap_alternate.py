def swap(li):
    l = len(li)

    if l%2==0:
        for i in range(0,l,2):
            li[i],li[i+1]=li[i+1],li[i]
    else:
        for i in range(0,l-1,2):
            li[i],li[i+1]=li[i+1],li[i]
    for i in li:
        print(i,end=' ')

b = input()

li = [int(x) for x in input().split()]
swap(li)