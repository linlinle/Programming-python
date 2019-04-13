

def merge_sort(list):
    if len(list) <=1:
        return list
    num = int(len(list)/2)
    left = merge_sort(list[:num])
    right = merge_sort(list[num:])
    return merge(left, right)

def merge(left, right):
    r, l = 0, 0
    result = []
    while l<len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result

print(merge_sort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))