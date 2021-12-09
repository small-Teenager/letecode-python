'''
53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分
链接：https://leetcode-cn.com/problems/maximum-subarray/
来源：力扣（LeetCode）
'''

# 暴力破解  动态规划
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)

        # 动态规划
        dp = []
        dp0 = nums[0]
        dp.append(dp0)
        for i in range(1, leng):
            dp1 = max(dp0, 0) + nums[i]
            dp.append(dp1)
            dp0 = dp1
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
