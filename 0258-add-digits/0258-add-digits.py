class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add(num):
            total=0
            fact=True
            while fact==True:
                if num>0 :
                    total+= num%10
                    num //= 10
                    if total>9:
                        total=add(total)
                else:
                    fact=False
                    return total
        result =add(num)
        return result

        