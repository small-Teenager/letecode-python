'''
36. 有效的数独
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-sudoku/
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """