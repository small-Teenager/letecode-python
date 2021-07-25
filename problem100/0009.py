'''
9. 回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number/
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        abs_x, rev = abs(x), 0
        while abs_x != 0:
            rev = rev * 10 + (abs_x % 10)
            abs_x //= 10
        return True if x == rev else False


a = Solution().isPalindrome(-123)
print(a)
