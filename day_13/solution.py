with open ('day_13/data.txt', 'r') as f:
  data = f.read().split('\n\n')

def mirror(grid):
  for r in range(1, len(grid)):
    above = grid[:r][::-1]
    below = grid[r:]

    above = above[:len(below)]
    below = below[:len(above)]

    if above == below:
      return r
  return 0

total = 0

for block in data:
  grid = block.splitlines()

  row = mirror(grid)
  total += row * 100

  col = mirror(list(zip(*grid)))
  total += col

print(total)