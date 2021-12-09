'''
350. 两个数组的交集 II
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
'''

# hash 遍历加入hash key:number value:frequency
# 遍历hash表 value>0 的值即为交集

class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = dict()
        for i in nums1:
            if i in nums2:
                if not i in hashmap:
                    hashmap[i] = [1, 0]
                else:
                    hashmap[i][0] += 1
        for j in nums2:
            if j in hashmap: hashmap[j][1] += 1

        ret = []
        for k, v in hashmap.items():
            ret.extend([k] * min(v))
        return ret
