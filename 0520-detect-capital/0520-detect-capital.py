class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        output=word.isupper() or word.islower() or word.istitle()
        return output
            
        
        