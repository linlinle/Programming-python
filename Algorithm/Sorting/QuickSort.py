
def quickSort(S, a, b):
  """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
  if a >= b:
    return S                                   # range is trivially sorted
  pivot = S[b]                                           # last element of range is pivot
  left = a                                               # will scan rightward
  right = b-1                                            # will scan leftward
  while left <= right:
    # scan until reaching value equal or larger than pivot (or right marker)
    while left <= right and S[left] < pivot:
      left += 1
    # scan until reaching value equal or smaller than pivot (or left marker)
    while left <= right and pivot < S[right]:
      right -= 1
    if left <= right:                                    # scans did not strictly cross
      S[left], S[right] = S[right], S[left]              # swap values
      left, right = left + 1, right - 1                  # shrink range

  # put pivot into its final place (此时left > right)
  S[left], S[b] = S[b], S[left]
  # make recursive calls
  quickSort(S, a, left - 1)
  quickSort(S, left + 1, b)

  return S


print(quickSort([27,38,13,49,76,97,65],0,6))