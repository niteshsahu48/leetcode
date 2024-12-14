class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        revers=0
        var=abs(x)

        while var!=0 and var>0:
            digit=var%10
            revers=revers*10+digit
            var//=10
           
            if -2**31 <= revers and revers>= 2**31 - 1 :
                return 0
        if x>0:
            return revers
        else:
            return -revers
            

            