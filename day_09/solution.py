with open('day_09/data.txt') as f:
  data = f.read().splitlines()

def extrapolate_1(arr):
  if all(x == 0 for x in arr):
    return 0

  deltas = [y - x for x, y in zip(arr, arr[1:])]
  diff = extrapolate_1(deltas)
  return arr[-1] + diff

def extrapolate_2(arr):
  if all(x == 0 for x in arr):
    return 0

  deltas = [y - x for x, y in zip(arr, arr[1:])]
  diff = extrapolate_2(deltas)
  return arr[0] - diff

total_1 = 0
total_2 = 0

for line in data:
  nums = list(map(int, line.split()))
  total_1 += extrapolate_1(nums)
  total_2 += extrapolate_2(nums)

print(total_1)
print(total_2)