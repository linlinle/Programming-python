"""
    题目链接：https://www.nowcoder.com/practice/661c49118ca241909add3a11c96408c8?tpId=85&tqId=29830&tPage=1&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking
    有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
"""

N = int(input())
ab = [int(x) for x in input().split()]
K,D = [int(x) for x in input().split()]

# dmax[i][j]表示前i个人中选j个人的最大值/最小值，第j个选择必须是i
dmax = [[0]*N for i in range(K)]
dmin = [[0]*N for j in range(K)]

res = (1 << 64) * -1


for i in range(N):                              # 选择第i个人
    dmax[0][i] = ab[i]
    dmin[0][i] = ab[i]
    # k=0已经初始化，直接从k=1开始
    for k in range(1,K):                        # 选择k个人
        for pre in  range(max(0,i-D),i):        # 在D约束条件下，与pre个可能的(k-1)个情况相乘选最大
            dmax[k][i] = max(dmax[k][i],max(dmax[k - 1][pre] * ab[i],dmin[k - 1][pre] * ab[i]))
            dmin[k][i] = min(dmin[k][i], min(dmax[k - 1][pre] * ab[i], dmin[k - 1][pre] * ab[i]))
    res = max(res, dmax[K - 1][i])

print(res)