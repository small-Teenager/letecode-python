'''
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
示例：
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/
'''
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = Counter(s)
        for i, j in enumerate(s):
            if d[j] == 1:
                return i
        return -1


s = Solution().firstUniqChar("loveleetcode")
print(s)
