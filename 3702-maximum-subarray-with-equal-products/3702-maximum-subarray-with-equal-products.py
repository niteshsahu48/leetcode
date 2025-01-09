class Solution:
    def maxLength(self, nums: List[int]) -> int:

        def lcm (a,b):
   	        return abs(a*b)//math.gcd(a,b)

        ans=1
        n=len(nums)
        if n==0:
            return 0

        for i in range(n):
            p=nums[i]
            g=nums[i]
            l=nums[i]
            for j in range(i+1,n):
                p*=nums[j]
                g=math.gcd(g,nums[j])
                l=lcm(l,nums[j])
                if p==(g*l):
                    ans=max(ans,j-i+1)
        return ans
        
        

        