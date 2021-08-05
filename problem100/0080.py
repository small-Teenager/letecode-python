'''
80. 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
来源：力扣（LeetCode）
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 变动1: 由于元素可以重复2次，left现在从第二个元素开始，right从第三个元素开始
        left = 1
        for right in range(2, len(nums)):
            # 变动2: 以前之和nums[left]比, 现在还要和nums[left - 1]比，从而保证元素可以重复两次
            if nums[right] == nums[left] and nums[right] == nums[left - 1]:
                continue
            left += 1
            nums[left] = nums[right]
        return left + 1


nums = [1, 1, 1, 2, 2, 3]
a = Solution().removeDuplicates(nums)
print(a)
