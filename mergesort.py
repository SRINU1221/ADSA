


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        low=0
        high=n-1
        self.mergesort(nums,low,high)
        return nums
    

    def mergesort(self,arr,low,high):
        if(low==high):
            return
        mid=(low+high)//2
        self.mergesort(arr,low,mid)
        self.mergesort(arr,mid+1,high)
        self.mergesortedarrays(arr,low,mid,high)
    

    def mergesortedarrays(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while(left<=mid and right<=high):
            if(arr[left]<arr[right]):
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while(left<=mid):
            temp.append(arr[left])
            left+=1

        while(right<=high):
            temp.append(arr[right])
            right+=1
        
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        
    
        


        
