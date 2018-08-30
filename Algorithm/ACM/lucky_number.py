"""
小明同学学习了不同的进制之后，拿起了一些数字做起了游戏。小明同学知道，在日常生活中我们最常用的是十进制数，而在计算机中，二进制数也很常用。
现在对于一个数字x，小明同学定义出了两个函数f(x)和g(x)。 f(x)表示把x这个数用十进制写出后各个数位上的数字之和。如f(123)=1+2+3=6。
g(x)表示把x这个数用二进制写出后各个数位上的数字之和。如123的二进制表示为1111011，那么，g(123)=1+1+1+1+0+1+1=6。
小明同学发现对于一些正整数x满足f(x)=g(x)，他把这种数称为幸运数，现在他想知道，大于0且小于等于n的幸运数有多少个？"""

def f(n, m):
    sum = 0
    while n:
        sum +=n%m
        n//=m
    return sum

if __name__ == "__main__":
    sum1 =0
    for i in range(1,int(input())+1):
        if f(i,2) == f(i,10):
            sum1 +=1
        else:
            continue

    # python 集成方法
    sum2 = 0
    for i in range(1,int(input())+1):
        binval = sum(map(int,list(bin(i).replace("0b",""))))
        decimalval = sum(map(int,list(str(i))))
        if decimalval == binval:
            sum2 +=1

    print(sum1,sum2)