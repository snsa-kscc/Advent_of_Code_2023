data_file = "day_03/data.txt"

with open(data_file, "r") as f:
  data = f.read().splitlines()

numbers = []
symbols = []

for row_num, line in enumerate(data):
  number = 0
  columns = []
  for col_number, c in enumerate(line.strip() + '.'):
    if c >='0' and c <= '9':
      number = number * 10 + int(c)
      columns.append(col_number)
    else:
      if number > 0:
        numbers.append((row_num, tuple(columns), number))
      if c != '.':
        symbols.append((row_num, col_number, c))
      number = 0
      columns = []

total = 0
offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for symbol in symbols:
  found = set()
  for number in numbers:
    for offset in offsets:
      location  = [symbol[0] + offset[0], symbol[1] + offset[1]]
      if number[0] == location[0] and location[1] in number[1]:
        found.add(tuple(number))
        break
  if len(found) == 2:
    value = 1
    for v in found:
      value *= v[2]
    total += value

print('part two', total)