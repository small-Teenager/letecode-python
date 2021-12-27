'''
167. 两数之和 II - 输入有序数组
给定一个已按照 非递减顺序排列 的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
'''


class Solution(object):
    # 双指针
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p, q = 0, len(numbers) - 1
        while p != q:
            if numbers[p] + numbers[q] == target:
                return [p + 1, q + 1]
            elif numbers[p] + numbers[q] > target:
                q -= 1
            else:
                p += 1
        return []


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
