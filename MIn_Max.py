# maximum and minimum element in arrray

#problem link --> https://practice.geeksforgeeks.org/problems/max-min/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

#Given an array A of size N of integers. Your task is to find the sum of minimum and maximum element in the array.

class Solution:
    def findSum(self,A,N):
        A.sort()                                   # Always run code in gfg or leetcode
        a = A[0]+A[-1]
        return a
        
       #return min(A)+max(A)     <------- We can use this approach too         

#driver codestarts
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
#driver code ends