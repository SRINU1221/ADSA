3658. GCD of Odd and Even Sums
Solved
Easy
premium lock icon
Companies
Hint
You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the first n odd numbers.

sumEven: the sum of the first n even numbers.

Return the GCD of sumOdd and sumEven.

 

Example 1:

Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=0
        even=0
        for i in range(1,n+1):
            odd=odd+(2*i-1)
            even=even+(2*i)
        
        return self.gcd(odd,even)
        
    
    # def gcd(self,a,b):
    #     l1=[]
    #     l2=[]
    #     for i in range(1,a+1):
    #         if(a%i == 0):
    #             l1.append(i)
    #     for i in range(1,b+1):
    #         if(b%i==0):
    #             l2.append(i)
        
    #     l=[]
    #     for i in range(len(l1)):
    #         l.append(l1[i])
    #     for i in range(len(l2)):
    #         l.append(l2[i])
        
    #     h={}
    #     for i in range(len(l)):
    #         if(l[i] in h):
    #             h[l[i]]+=1
    #         else:
    #             h[l[i]]=1
        
    #     ml=[]
    #     for i,j in h.items():
    #         if(j==2):
    #             ml.append(i)
        
    #     return max(ml)

    #using ecludian formula
    def gcd(self,a,b):
        while(b!=0):
            r=a%b
            a=b
            b=r
        
        return a
        
