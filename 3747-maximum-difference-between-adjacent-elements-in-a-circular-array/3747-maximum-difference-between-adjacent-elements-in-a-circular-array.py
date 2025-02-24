class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)
        #print(n)
        max_first=abs(nums[0]-nums[n-1])
        #print(max_first)
        #print(nums[n-1])
        diff=0

        for i in range (1,n):
            diff=abs(nums[i]-nums[i-1])
            max_first=max(max_first,diff)
        return max_first
        