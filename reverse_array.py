# Write a program to reverse an array or string

# Reverse words in a given string

# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

#problem link-->https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab



#code

# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        x = S.split(".")           
        b = x[::-1]                   
        c = ".".join(b)
        return c
      # return ".".join(S.split(".")[::-1])   <-------- one line approach of above code
        
        




#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends