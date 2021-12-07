'''
217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
链接：https://leetcode-cn.com/problems/contains-duplicate/
来源：力扣（LeetCode）
'''


class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # set天然去重
        # return len(nums) != len(set(nums))

        # hash表
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         return True
        #     dic[i] = 1
        # return False

        # 排序后比较相邻两个值
        nums.sort()
        l = len(nums)
        tab = 0
        for i in range(0, l - 1):
            if nums[i] == nums[i + 1]:
                tab = 1
                break
        if tab == 1:
            return True
        return False


nums = [1, 2, 3, 1]
print(nums)
b = Solution().containsDuplicate(nums)
print(b)
