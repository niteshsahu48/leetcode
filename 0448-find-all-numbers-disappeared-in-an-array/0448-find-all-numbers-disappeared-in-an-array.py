class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        best=set(nums)
        output=[]
        length = len(nums)
        for i in range (1,length+1):
            if i not in best:
                output.append(i)
        return output

                
        