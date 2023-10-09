#Selection Sort

from sys import stdin

def selectionSort(arr) :
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]
    
    return arr
    #Your code goes here



n = int(input())
arr = [int(x) for x in input().split()]

A = selectionSort(arr)

for k in A:
    print(k, end=' ')
