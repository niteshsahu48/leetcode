class Solution:
    def mySqrt(self, x: int) -> int:

        """for i in range(0,n+1):
            if i*i==n: return i 
            if i*i>n:
                return i-1"""
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last


        
        