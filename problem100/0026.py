'''
26. 删除有序数组中的重复项
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
来源：力扣（LeetCode）
'''


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        for right in range(len(nums)):
            # 如果相等, 说明right指向的元素是重复元素，不保留
            if nums[right] == nums[left]:
                continue

            # 如果不相等, 说明right指向的元素不是重复元素，保留，然后右移left一个单位，再把right的值赋给left
            left += 1
            nums[left] = nums[right]
        return left + 1



a = Solution().removeDuplicates([1, 2, 3, 3])
print(a)

