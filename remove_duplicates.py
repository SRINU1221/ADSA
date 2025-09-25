class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # take two pointers and whare the first pointer is point to first element hence it is fixed and take another pointer which is at first place now move the second pointer and compare the first pointer if they are not equal then then place that second pointer element at the first pointer place 
        n=len(nums)
        i=0
        for j in range(1,n):
            if(nums[j]!=nums[i]):
                nums[i+1]=nums[j]
                i+=1
        return i+1

        
