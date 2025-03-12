class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        if a != b:
            return (max(len(b),len(a)))
        if a not in b:
            return(max(len(b),len(a)))
        