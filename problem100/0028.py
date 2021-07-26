'''
28. 实现 strStr()
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
来源：力扣（LeetCode）
'''

class Solution(object):
    # slow
    def strStr(self, haystack, needle):
        """
       :type haystack: str
       :type needle: str
       :rtype: int
       """
        if not needle:
            return 0
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1
    # fast
    def strStr_fast(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        return haystack.find(needle)


a = Solution().strStr('hello', 'll')
print(a)
b = Solution().strStr_fast('hello', 'll')
print(a)
