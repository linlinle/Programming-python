"""
源自 ：http://www.hawstein.com/posts/dp-novice-to-advanced.html
动态规划入门
"""

def fewest_coins(n):
    """
    面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
    :状态 : d(i) = j 表示凑够i元最少需要j个硬币
    :状态转移方程: d(i) =min{d(i-vj)+1}
    :解释: 所有之前一个硬币之差的最优解的最小值
    """
    Min = [i for i in range(n+1)]
    coins = [1,3,5]
    for i in range(1,n+1):
        for j in coins:
            if Min[i-j]+1 < Min[i] and j<=i:
                Min[i] = Min[i-j]+1

    return Min[n]


def LIS(A):
    """
    一个序列有N个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度
    :状态:           d(i)，表示前i个数中以A[i]结尾的最长非降子序列的长度
    :状态转移方程:    d(i) = max{1, d(j)+1},其中j<i,A[j]<=A[i]
    :解释：就把i前面的各个子序列中， 最后一个数不大于A[i]的序列长度加1，然后取出最大的长度即为d(i)
    """
    n = len(A)
    d = [1]*n
    max_len =1
    for i in range(n):
        for j in range(i):
            if A[j]<A[i] and d[j]+1 > d[i]:
                d[i] = d[j]+1
        if d[i]>max_len:
            max_len=d[i]

    return max_len

def grid_apple(A):
    """
    平面上有N*M个格子，每个格子中放着一定数量的苹果。你从左上角的格子开始， 每一步只能向下走或是向右走，每次走到一个格子上就把格子里的苹果收集起来， 这样下去，你最多能收集到多少个苹果。
    :状态:        S[i][j]表示我们走到(i, j)这个格子时，最多能收集到多少个苹果
    :状态转换:     S[i][j]=A[i][j] + max(S[i-1][j], if i>0 ; S[i][j-1], if j>0),A[i][j]代表格子(i, j)处的苹果数量
    :解释:到达一个格子的方式最多只有两种：从左边来的(除了第一列)和从上边来的(除了第一行)
    """
    m,n = len(A),len(A[0])
    S = [[0]*n]*m
    S[0][0] = A[0][0]

    for i in range(m):
        for j in range(n):
            if i ==0 and j>0:
                S[i][j] = A[i][j] + S[i][j - 1]
            if j ==0 and i >0:
                S[i][j] = A[i][j] + S[i-1][j]
            if i >0 and j>0:
                S[i][j] = A[i][j]+max(S[i-1][j],S[i][j-1])

    return max(max(S))

if __name__ == "__main__":
    A = [[1,1,1,1],
         [10,1,10,0],
         [1,1,0,0]]
    print(grid_apple(A))