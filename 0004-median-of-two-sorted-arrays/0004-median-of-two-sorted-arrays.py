class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums3=sorted(nums1)
        length = len(nums3)
        mid = length // 2
        if length % 2 != 0:
            return nums3[mid]
        else:
            return (nums3[mid-1] + nums3[mid]) / 2
