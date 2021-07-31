'''
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
链接：https://leetcode-cn.com/problems/powx-n/
来源：力扣（LeetCode）
'''


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:  # 通过折半计算，每次把 n 减半，降低时间复杂度
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                res *= x
                n -= 1
        return res

    # 位运算
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


a = Solution().myPow(2, 3)
print(a)
b = Solution().myPow2(2, 3)
print(a)
