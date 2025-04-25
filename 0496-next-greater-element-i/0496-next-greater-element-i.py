class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        next_greater = {}
        stack = []
            
            # Traverse nums2 and fill the next_greater map
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
            
        # Any elements remaining in the stack don't have a next greater element
        while stack:
            next_greater[stack.pop()] = -1
            
        # Step 2: Answer the queries for each element in nums1
        return [next_greater[num] for num in nums1]

       
