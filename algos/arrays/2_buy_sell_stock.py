from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_pro = 0
        # for i in range(len(prices)):
        #     for k in range(i + 1, len(prices)):
        #         if prices[i] > prices[k]:
        #             continue

        #         profit = prices[k] - prices[i]
        #         if max_pro < profit:
        #             max_pro = profit

        # return max_pro

        max_profit = 0
        min_so_far = float('inf')
        for i in range(len(prices)):
            profit = prices[i] - min_so_far
            if profit > max_profit:
                max_profit = profit
            
            if min_so_far > prices[i]:
                min_so_far = prices[i]
        
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
