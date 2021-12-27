'''
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string/
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 初始化双指针
        left = 0
        right = len(s) - 1

        # 这种方法可以不用判断元素奇偶
        while left < right:
            s[left], s[right] = s[right], s[left]

            # 交换后，左指针右移，右指针左移
            left += 1
            right -= 1
        # return s


s = ["h", "e", "l", "l", "o"]
s = Solution().reverseString(s)
print(s)
