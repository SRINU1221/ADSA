

class Solution:
    def triplets(self, arr ):
        # code 
        n=len(arr)
        arr.sort()
        res=[]
        for i in range(0,n-2):
            #remove duplicates
            if(i>0 and arr[i]==arr[i-1]):
                continue
                
    
            left=i+1
            right=n-1
            
            while(left<right):
                ts=arr[i]+arr[left]+arr[right]
                if(ts== 0):
                    res.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                    while(left<right and arr[left]==arr[left-1]):
                        left+=1
                    while(left<right and arr[right]==arr[right+1]):
                        right-=1
                    
                    
                elif(ts < 0):
                    left+=1
                else:
                    right-=1
                
        
        return res
                
        
