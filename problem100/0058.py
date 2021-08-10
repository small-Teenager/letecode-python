'''
58. 最后一个单词的长度
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串
链接：https://leetcode-cn.com/problems/length-of-last-word/
来源：力扣（LeetCode）
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for char in s.strip()[::-1]:
            if char == ' ':
                return ans
            ans += 1
        return ans


a = Solution().lengthOfLastWord('hello world ')
print(a)
