class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp =(x)
        reverse = 0
        while x!=0 and x>0:
            digit = x%10
            reverse=reverse*10+digit
            x//=10
        if temp==reverse:
            return True
        else:
            return False
           



           