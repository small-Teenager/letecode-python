'''
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
'''


class Solution(object):
    # 图片中绘制数组
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inf = int(1e9)
        minPrice = inf
        maxProfit = 0
        for price in prices:
            maxProfit = max(price - minPrice, maxProfit)
            minPrice = min(price, minPrice)
        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
