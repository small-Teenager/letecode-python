'''
567. 字符串的排列
给你两个字符串s1和s2 ，写一个函数来判断 s2 是否包含 s1的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
'''
import collections


class Solution(object):
    # 滑动窗口
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # s1比s2长时，一定不能匹配
        n1, n2 = len(s1), len(s2)
        if len(s1) > len(s2): return False
        # 首先统计s1中所含元素
        freq1 = collections.Counter(s1)
        # 初始化s2前n1-1长度中所含元素，这时初始的窗口大小比s1小1
        freq2 = collections.Counter(s2[:n1 - 1])
        # 滑动窗口，窗口大小为s1的长度，每一步中加入右边元素，删除左边元素
        left, right = 0, n1 - 1
        # 窗口最多移动到s2的末尾
        while right < n2:
            # 加上右边元素，这时窗口大小与s1相同
            freq2[s2[right]] += 1
            # 这时判断是否相等
            if freq1 == freq2:
                return True
            # 删除左边元素
            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            # 窗口进行移动
            left += 1
            right += 1
        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
