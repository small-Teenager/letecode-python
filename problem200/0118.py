'''
118. 杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
'''
from math import factorial as f  # 导入math库中的计算阶乘的方法factorial


class Solution(object):
    """
    数学解法 杨辉三角的公式
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 运用杨辉三角的公式:第n行第m个数可表示为C(n-1，m-1) = (n - 1)!/(m - 1)!*(n - m - 2)!
        res = [[] for _ in range(numRows)]  # 用列表推导式初始化
        if not numRows: return []  # 如果numRows == 0则直接返回[]

        for i in range(numRows):  # 遍历每一行
            for j in range(i + 1):  # 遍历每一行的数
                res[i].append(f(i) // (f(j) * f(i - j)))
                """
                注意这里直接用i,j就行了,而不是杨辉三角公式所示的n - 1, m -1。
                """
        return res


print(Solution().generate(8))
