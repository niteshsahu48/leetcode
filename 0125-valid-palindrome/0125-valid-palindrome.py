class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        backword=''
        add="".join([item for item in s if item.isalnum()])
        print(add)
        for i in add:
            backword=i+backword
        if backword==add:
            return True
        else:
            return False


        