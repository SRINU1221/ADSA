#User function Template for python3

class Solution:
    def rotate(self, arr):
        n=len(arr)
        #anti clockwise direction rotation by one place 
        # temp=arr[0]
        # for i in range(1,n):
        #     arr[i-1]=arr[i]
        
        # arr[n-1]=temp
        # return arr
        
        #clockwise direction rotate by one place
        temp=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        
        arr[0]=temp
        return arr
    
