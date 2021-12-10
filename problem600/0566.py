'''
566. 重塑矩阵
在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
给你一个由二维数组 mat 表示的m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reshape-the-matrix
'''


class Solution(object):
    # 二维降一维 一维升二维
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        k = [mat[i][j] for i in range(m) for j in range(n)]
        mat = []
        h = []
        for i in range(len(k)):
            h.append(k[i])
            if (i + 1) % c == 0:
                mat.append(h)
                h = []
        return mat


mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(Solution().matrixReshape(mat=mat, r=1, c=4))
