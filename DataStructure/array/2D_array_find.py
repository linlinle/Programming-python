"""在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。"""

class Solution:
    def Find_lower_left(self,target,array):

        #找出最大行列
        cols = len(array[0])-1
        rows = len(array)-1

        # 设置i，j为起始位置(左下角)
        i = rows
        j=0

        #最大边界检测
        while j<=cols and i>=0:
            if target>array[i][j]:
                j +=1
            elif target<array[i][j]:
                i -=1
            else:
                return True

        return False

    def Find_upper_right(self,target,array):

        rows = len(array)-1
        cols = len(array[0])-1

        i = 0
        j = cols

        while i<=rows and j >=0:
            if target>array[i][j]:
                i +=1
            elif target< array[i][j]:
                j -=1
            else:
                return True

        return False


if __name__=="__main__":
    solution = Solution()
    target = 12
    array = [[1,3,5],[7,9,11],[13,15,17]]
    array_1 = [[2,4,6],[8,10,12],[14,16,18]]
    print(solution.Find_lower_left(target,array))
    print(solution.Find_lower_left(target,array_1))