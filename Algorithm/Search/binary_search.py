# -*- coding: utf-8 -*-

def binary_search(data,target,low,hight):
    '''二分查找  O(log(N))'''
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


def binary_search_sorted(data,target,low,hight):
    '''二分查找'''
    if low > hight:
        return False
    while low <= hight:
        mid = (low+hight)//2
        if target < data[mid]:
            hight = mid -1
        elif target > data[mid]:
            low = mid + 1
        else:
            return True

    return False


if __name__ == '__main__':
    find_list = list(range(1,22,2))
    print(find_list)
    print(binary_search_sorted(find_list,1,0,len(find_list)-1))