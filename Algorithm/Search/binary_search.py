# -*- coding: utf-8 -*-
'''二分查找  O(log(N))'''

def binary_search(data,target,low,hight):
    if low > hight:
        return False
    else:
        mid = (low+hight)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,hight)


if __name__ == '__main__':
    find_list = list(range(1,22))
    print(find_list)
    print(binary_search(find_list,17,0,22))