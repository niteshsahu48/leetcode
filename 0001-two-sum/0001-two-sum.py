class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        total = [] 
        for i in range (len(nums)): 
	        for j in range (i+1,len(nums)):
		        if nums[i] + nums[j] ==target:
			        total.append(i)
			        total.append(j)
        return total
        