class Solution(object):
    def longestCommonPrefix(self,strs):
        if not strs: 
    	    return ""
        for i in range(len(strs[0])):
    	    #print(strs[i])
    	    char = strs[0][i]
    	    for j in range(1,len(strs)):
    		    print(j)

        	    if i==len(strs[j]) or  strs[j][i] != char:
        		    #print(strs[j][i])
        		    return strs[0][:i]
        return strs[0]
	   
        
    
