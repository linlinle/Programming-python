
def quickSort(S, a, b):
  if a >= b:
    return S
  pivot = S[b]
  left = a
  right = b-1
  while left <= right:
    while left <= right and S[left] < pivot:
      left += 1
    while left <= right and pivot < S[right]:
      right -= 1
    if left <= right:
      S[left], S[right] = S[right], S[left]
      left, right = left + 1, right - 1

  # put pivot into its final place (此时left > right)
  S[left], S[b] = S[b], S[left]
  quickSort(S, a, left - 1)
  quickSort(S, left + 1, b)

  return S


print(quickSort([27,38,13,49,76,97,65],0,6))