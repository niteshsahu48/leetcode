class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """var=0
        if len(prices)==1:
            return 0

        else:
            for i in range(len(prices:
                if i<i+1:
                    if i+1>i+2:
                        var+=i
        #else:
            #new_prices = sorted(prices)
            #var=new_prices[0]
        index=0
        
        #print(new_prices)
        #print(new_prices[0])
        while prices[index]!=var :
            prices.remove(prices[index])
        prices.sort()
        return(prices[-1]-var)"""

        """if len(prices)==1:
            return(0)
        else:
            index=0
            while len(prices):
                if prices[index]<prices[index+1]:
                    if prices[index+1]>prices[index+2]:
                        buy=prices[index]
                        sale=prices[index+1]
                        break
                else:
                    index+=1
            return(sale-buy)"""

        start=1
        end=0
        total_profit=0
        while start <len(prices):
            profit=prices[start]-prices[end]
            if prices[end]<prices[start]:
                total_profit=max(profit,total_profit)
            else:
                end=start
            start+=1
        return total_profit


    
            