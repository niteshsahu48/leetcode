class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """if needle in haystack:
            temp=haystack.index(needle)
            return temp
        else:
            return -1"""
        for i in range(len(haystack) - len(needle) + 1):
            #print(i)
            #print(len(haystack) - len(needle) + 1)
            if haystack[i:i+len(needle)] == needle:
                #print(haystack[i:i+len(needle)])
                #print(i+len(needle))
                return i 
        return -1
        