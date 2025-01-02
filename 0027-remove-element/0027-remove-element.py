class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count= "_"
        for i in range (len(nums)):
            #print(nums[i])
            if val in nums:
                nums.remove(val)
                #nums.append(count)
        #nums.append(count)
        return (len(nums))

        