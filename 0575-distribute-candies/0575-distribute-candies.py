class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy=int(len(candyType)/2)
        length=len(set(candyType))
        return min(candy,length)
        

        