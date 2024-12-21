class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        list1=[]
        for i in digits:
            s+=str(i)
        add=int(s)+1
        for i in str(add):
            list1.append(int(i))
        return list1