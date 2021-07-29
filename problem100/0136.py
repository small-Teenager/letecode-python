'''
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
链接：https://leetcode-cn.com/problems/single-number/
来源：力扣（LeetCode）
'''
from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res = res ^ i
        return res
        # return reduce(lambda x, y: x ^ y, nums)


a = Solution().singleNumber([2, 2, 1])
print(a)
