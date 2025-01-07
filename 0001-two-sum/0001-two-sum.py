class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = [] 
        for i in range (len(nums)): 
	        for j in range (i+1,len(nums)):
		        if nums[i] + nums[j] ==target:
			        total.append(i)
			        total.append(j)
        return total
        