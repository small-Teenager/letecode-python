'''
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
链接：https://leetcode-cn.com/problems/search-insert-position/
来源：力扣（LeetCode）
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if target > nums[length - 1]:
            return length
        for i, ele in enumerate(nums):
            if ele == target:
                return i
            elif ele > target:
                return i


a = Solution().searchInsert([1, 3, 5, 6], 7)
print(a)
