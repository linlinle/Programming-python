import math

def merge(src, result, start, inc):
  """合并src[start:start+inc] 与 src[start+inc:start+2*inc]"""
  end1 = start+inc
  end2 = min(start+2*inc, len(src))
  x, y, z = start, start+inc, start

  #下面循环结束的条件有两个，如果是左边的游标尚未到达，那么需要把数组接回去，可能会有疑问，那如果右边的没到达呢，其实模拟一下就可以
  # 知道，如果右边没到达，那么说明右边的数据比较大，这时也就不用移动位置了

  while x < end1 and y < end2:            #如果左边的数据还没达到分割线且右边的数组没到达分割线，开始循环
    if src[x] < src[y]:
      result[z] = src[x]
      x += 1
    else:
      result[z] = src[y]
      y += 1
    z += 1
  if x < end1:
    result[z:end2] = src[x:end1]
  elif y < end2:
    result[z:end2] = src[y:end2]

def merge_sort(S):

  n = len(S)
  logn = math.ceil(math.log(n,2))
  src, dest = S, [None] * n
  for i in (2**k for k in range(logn)):     #逐级上升，第一次比较2个，第二次比较4个，第三次比较8个。。。
    for j in range(0, n, 2*i):
      merge(src, dest, j, i)
    src, dest = dest, src
  if S is not src:
    S[0:n] = src[0:n]
