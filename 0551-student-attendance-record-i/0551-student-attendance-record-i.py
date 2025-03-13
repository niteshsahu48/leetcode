class Solution:
    def checkRecord(self, s: str) -> bool:
        count_l=0
        count_a=0
        for i in s:
            if i=="A":
                count_a+=1
            elif i=="L":
                count_l+=1
        if count_a>=2 :
            return False
        elif "LLL" in s:
            return False
        else:
            return True

        