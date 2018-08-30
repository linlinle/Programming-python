"""
有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。请设计一个算法，计算小团有多少种走法。给定两个正整数int x,int y，请返回小团的走法数目。
"""
def factorial(x):
    fac = 1
    for i in range(1,x+1):
        fac *= i
    return fac
def by_factorial(m,n):
    """
    做左上角走到右下角，需要x次向右，y次像左走:C{x}{x+y}=C{y}{x+y}=(x+y)!//x!y!
    """
    return factorial(m+n)//factorial(m)//factorial(n)


def by_daynamic_programming(m,n):
    """
     "状态"：        dp[i][j]表示(i,j)位置一共有多少种走法,
     "初始状态"：    由于只能向左和向右走，所以第一列和第一行所有位置的走法都是1，即dp[i][0]=1,dp[0][j]=1(0=<i<=x,0<=j<=y)，
     "状态转换"：    对于其他位置，走法应该等于其左边格点的走法和其上面格点的走法之和，dp[i][j]=dp[i-1][j]+dp[i][j-1]，
    """
    mn = [[0] * (n+1)]*(m+1)
    for i in range(m+1):
        mn[i][0] = 1
    for j in range(n+1):
        mn[0][j] =1
    for i in range(1,m+1):
        for j in range(1,n+1):
            mn[i][j] = mn[i-1][j]+mn[i][j-1]
    return mn[m][n]


def by_recursion(m,n):
    """
    递归方法，回溯效果，类似动态规划的反向效果
    """
    if m==0 or n==0:
        return 1
    return by_recursion(m-1,n)+by_recursion(m,n-1)




if __name__ == "__main__":
    m,n = [int(x) for x in input().split()]
    print(by_recursion(m,n))