class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        ans = 1
        for i in range (2,int(num**0.5)+1):
            if num % i == 0:
                ans += i + num // i
        return ans == num

        """l=[]
        if(num%2==1):
            return False

        for i in range(1,num//2+1):
            if(num%i==0):
                l.append(i)
        if(sum(l)==num):
            return True
        return False"""

        