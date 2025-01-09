class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range (len(nums)):
            #print(nums[i])
            if val in nums:
                nums.remove(val)
                #nums.append(count)
        #nums.append(count)
        return (len(nums))
        