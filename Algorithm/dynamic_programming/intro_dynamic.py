# -*- coding: utf-8 -*-
"""
源自 ：http://www.hawstein.com/posts/dp-novice-to-advanced.html
动态规划入门
"""
import unittest

def fewest_coins(total):
    """
    面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
    :状态 : d(i) = j 表示凑够i元最少需要j个硬币
    :状态转移方程: d(i) =min{d(i-vj)+1}
    :解释: 所有之前一个硬币之差的最优解的最小值
    """
    dynamic_subsequence = [i for i in range(total + 1)]
    coins = [1,3,5]
    for i in range(1, total + 1):
        for j in coins:
            if dynamic_subsequence[i-j]+1 < dynamic_subsequence[i] and j<=i:
                dynamic_subsequence[i] = dynamic_subsequence[i-j]+1
    return dynamic_subsequence[total]

def LIS(sequence):
    """
    一个序列有N个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度
    :状态:           d(i)，表示前i个数中以A[i]结尾的最长非降子序列的长度
    :状态转移方程:    d(i) = max{1, d(j)+1},其中j<i,A[j]<=A[i]
    :解释：就把i前面的各个子序列中， 最后一个数不大于A[i]的序列长度加1，然后取出最大的长度即为d(i)
    """
    n = len(sequence)
    dynamic_subsequence = [1]*n
    max_len =1
    for i in range(n):
        for j in range(i):
            if sequence[j]<sequence[i] and dynamic_subsequence[j]+1 > dynamic_subsequence[i]:
                dynamic_subsequence[i] = dynamic_subsequence[j]+1
        if dynamic_subsequence[i]>max_len:
            max_len=dynamic_subsequence[i]
    return max_len

def grid_collect_apple(grid):
    """
    平面上有N*M个格子，每个格子中放着一定数量的苹果。你从左上角的格子开始， 每一步只能向下走或是向右走，每次走到一个格子上就把格子里的苹果收集起来， 这样下去，你最多能收集到多少个苹果。
    :状态:        S[i][j]表示我们走到(i, j)这个格子时，最多能收集到多少个苹果
    :状态转换:     S[i][j]=A[i][j] + max(S[i-1][j], if i>0 ; S[i][j-1], if j>0),A[i][j]代表格子(i, j)处的苹果数量
    :解释:到达一个格子的方式最多只有两种：从左边来的(除了第一列)和从上边来的(除了第一行)
    """
    m,n = len(grid), len(grid[0])
    dynamic_subsequence = [[0]*n]*m
    dynamic_subsequence[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i ==0 and j>0:
                dynamic_subsequence[i][j] = grid[i][j] + dynamic_subsequence[i][j - 1]
            if j ==0 and i >0:
                dynamic_subsequence[i][j] = grid[i][j] + dynamic_subsequence[i - 1][j]
            if i >0 and j>0:
                dynamic_subsequence[i][j] = grid[i][j] + max(dynamic_subsequence[i - 1][j], dynamic_subsequence[i][j - 1])
    return max(max(dynamic_subsequence))

class introDynamicTestCase(unittest.TestCase):

    def setUp(self):
        self.grid = [[1, 1, 1, 1], [10, 1, 10, 0], [1, 1, 0, 0]]
        self.sequence = [1,2,3,4,11,6,7,8,9]
        self.total = 11

    def test_grid_collect_apple(self):
        self.assertEqual(grid_collect_apple(self.grid), 22)

    def test_LIS(self):
        self.assertEqual(LIS(self.sequence),8)

    def test_fewest_coins(self):
        self.assertEqual(fewest_coins(self.total),3)

unittest.main()
