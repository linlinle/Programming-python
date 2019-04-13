
def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        # 将S1和S2元素重新写入并覆盖掉S，可以将S看作新的空列表
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
          S[i+j] = S1[i]
          i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(S):
    """利用数组实现"""
    n = len(S)
    if n < 2:
        return S
    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
