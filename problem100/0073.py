'''
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes/
'''


class Solution(object):
    # 第一次遍历标记位置，第二次进行modify
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        loc = list()  # 记录matrix中值为0的index
        m, n = len(matrix), len(matrix[0])  # 获取matrix维度
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    loc.append([i, j])
        if loc:
            a, b = zip(*loc)
        else:
            return matrix
        # 对行和列上为0的loc分别赋值
        for i in a:
            for j in range(n):
                matrix[i][j] = 0
        for i in b:
            for j in range(m):
                matrix[j][i] = 0
        return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print("----------old matrix-----------")
for i in matrix:
    print(i)
print("----------new matrix-----------")
Solution().setZeroes(matrix)
for i in matrix:
    print(i)
