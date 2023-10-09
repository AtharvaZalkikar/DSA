
from sys import stdin


def mergetwoarrays(a1,a2):
    i,j=0,0
    len1,len2 = len(a1),len(a2)
    new_array = []
    
    while (i<len1 and j<len2):
        if a1[i]<a2[j]:
            new_array.append(a1[i])
            i = i+1
        else:
            new_array.append(a2[j])
            j = j+1
            
    while (i<len1):
        new_array.append(a1[i])
        i = i+1
    
    while (j<len2):
        new_array.append(a2[j])
        j = j+1
    return new_array

a1 = [1,3,4,7,11]
a2 = [4,9,11,13,15,17]
new_array = mergetwoarrays(a1,a2)
print(new_array)