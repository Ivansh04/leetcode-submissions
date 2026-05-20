class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        mi=prices[0]
        for i in range(1,len(prices)):
            p=prices[i]-mi
            m=max(m,p)
            mi=min(prices[i],mi)
        return m

        