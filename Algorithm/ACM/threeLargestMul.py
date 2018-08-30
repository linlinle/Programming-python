# -*- coding: utf-8 -*-
'''输入一组数，找出三个相乘最大的值'''
def getLargestMul(array):
    max1 = 0; max2 = 0; max3 = 0;min1 = 0; min2 = 0
    for i in array:
        if i !=0:
            if i>max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i>max2:
                max3 = max2
                max2 = i
            elif i>max3:
                max3 = i
            elif i<min1:
                min2 = min1
                min1 = i
            elif i<min2:
                min2 = i
        else:continue
    maximuix = max((max1*max2*max3),(max1*min1*min2))
    print(maximuix)

if __name__=="__main__":
    line1 =int( input().strip('\n'))
    line2 = input().strip('\n').split(' ')
    arr = []
    for i in line2:
        arr.append(int(i))
    getLargestMul(arr)